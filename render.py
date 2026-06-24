from pathlib import Path

from mako.lookup import TemplateLookup

BASE_DIR = Path(__file__).parent

template_lookup = TemplateLookup(directories=[str(BASE_DIR)])


def render_index(config):
    template = template_lookup.get_template("index.mako")
    return template.render(**config)
