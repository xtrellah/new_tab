import os
import tomllib
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse

from mako.lookup import TemplateLookup

HOST = "localhost"
PORT = int(os.environ.get("PORT", "60065"))
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


class NewTabHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        path = urlparse(self.path).path

        if path == "/":
            self.render_index()
            return

        super().do_GET()

    def render_index(self):
        template = template_lookup.get_template("index.mako")
        body = template.render(**load_links()).encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


server = HTTPServer((HOST, PORT), NewTabHandler)

print(f"Serving at http://{HOST}:{PORT}")
server.serve_forever()
