import os
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse

from mako.lookup import TemplateLookup

HOST = "localhost"
PORT = int(os.environ.get("PORT", "60065"))
BASE_DIR = Path(__file__).parent

template_lookup = TemplateLookup(directories=[str(BASE_DIR)])


class NewTabHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        path = urlparse(self.path).path

        if path == "/":
            self.render_index()
            return

        super().do_GET()

    def render_index(self):
        template = template_lookup.get_template("index.mako")
        body = template.render().encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


server = HTTPServer((HOST, PORT), NewTabHandler)

print(f"Serving at http://{HOST}:{PORT}")
server.serve_forever()
