import re
import tomllib
from pathlib import Path

from mako.lookup import TemplateLookup

BASE_DIR = Path(__file__).parent
CONFIG_FILE = BASE_DIR / "config.toml"
COMPONENT_TABLE_PATTERN = re.compile(r"^\s*\[\[\s*([A-Za-z0-9_-]+)\s*\]\]\s*(?:#.*)?$")
SUPPORTED_COMPONENTS = {"github_section", "search_bar", "card_section"}

template_lookup = TemplateLookup(directories=[str(BASE_DIR)])


def load_config():
    config_text = CONFIG_FILE.read_text(encoding="utf-8")
    data = tomllib.loads(config_text)

    return {"components": build_components(data, parse_component_sequence(config_text))}


def build_components(data, component_sequence):
    component_config = {
        "github_section": parse_github_sections(data.get("github_section", [])),
        "search_bar": parse_search_bars(data.get("search_bar", [])),
        "card_section": parse_card_sections(data.get("card_section", [])),
    }
    component_indexes = dict.fromkeys(component_config, 0)
    components = []

    for component_type in component_sequence:
        component_index = component_indexes[component_type]
        sections = component_config[component_type]

        if component_index >= len(sections):
            raise ValueError(
                f"config.toml contains more {component_type} headers than configured sections"
            )

        components.append(
            {
                "type": component_type,
                "config": sections[component_index],
            }
        )
        component_indexes[component_type] += 1

    return components


def parse_component_sequence(config_text):
    component_sequence = []

    for line in config_text.splitlines():
        match = COMPONENT_TABLE_PATTERN.match(line)
        if not match:
            continue

        component_name = match.group(1)
        if component_name in SUPPORTED_COMPONENTS:
            component_sequence.append(component_name)

    return component_sequence


def parse_github_sections(sections):
    return [
        {
            "items": parse_link_or_pipe_items(
                section.get("items", []),
                "github_section.items",
            )
        }
        for section in sections
    ]


def parse_search_bars(sections):
    search_bars = []

    for section in sections:
        search_bars.append(
            {
                "action": section.get("action", "https://www.google.com/search"),
                "method": section.get("method", "GET"),
                "name": section.get("name", "q"),
                "placeholder": section.get("placeholder", "Search"),
                "autocomplete": section.get("autocomplete", "off"),
                "autofocus": section.get("autofocus", False),
                "required": section.get("required", True),
            }
        )

    return search_bars


def parse_card_sections(sections):
    return [
        {
            "title": section.get("title", "Links"),
            "items": parse_link_items(section.get("items", []), "card_section.items"),
        }
        for section in sections
    ]


def parse_link_or_pipe_items(items, section_name):
    parsed_items = []

    for item in items:
        if item == ["|"]:
            parsed_items.append({"type": "pipe"})
            continue

        label, href = parse_link_tuple(item, section_name)
        parsed_items.append({"type": "link", "label": label, "href": href})

    return parsed_items


def parse_link_items(items, section_name):
    links = []

    for item in items:
        label, href = parse_link_tuple(item, section_name)
        links.append({"label": label, "href": href})

    return links


def parse_link_tuple(item, section_name):
    if not isinstance(item, list) or len(item) != 2:
        raise ValueError(f"{section_name} entries must be [label, href] tuples")

    label, href = item

    if not isinstance(label, str) or not isinstance(href, str):
        raise ValueError(f"{section_name} tuple values must be strings")

    return label, href


def render_index():
    template = template_lookup.get_template("index.mako")
    return template.render(**load_config())
