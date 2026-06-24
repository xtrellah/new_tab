import os
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse

from parser import load_config
from render import render_index

HOST = "localhost"
PORT = int(os.environ.get("PORT", "60065"))


class NewTabHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        path = urlparse(self.path).path

        if path == "/":
            self.render_index()
            return

        super().do_GET()

    def render_index(self):
        tab_config = load_config()

        body = render_index(tab_config).encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def main():
    server = HTTPServer((HOST, PORT), NewTabHandler)
    print(f"Serving at http://{HOST}:{PORT}")

    server.serve_forever()


if __name__ == "__main__":
    main()
