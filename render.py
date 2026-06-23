import tomllib
from pathlib import Path

from mako.lookup import TemplateLookup

BASE_DIR = Path(__file__).parent
LINKS_FILE = BASE_DIR / "links.toml"

template_lookup = TemplateLookup(directories=[str(BASE_DIR)])


def load_links():
    with LINKS_FILE.open("rb") as links_file:
        data = tomllib.load(links_file)

    return {
        "github_links": parse_links(data.get("github_links", []), "github_links"),
        "link_cards": parse_links(data.get("link_cards", []), "link_cards"),
    }


def parse_links(items, section_name):
    links = []

    for item in items:
        try:
            label = item["label"]
            href = item["href"]
        except KeyError as exc:
            raise ValueError(
                f"{section_name} entries must include label and href"
            ) from exc

        links.append((label, href))

    return links


def render_index():
    template = template_lookup.get_template("index.mako")
    return template.render(**load_links())
