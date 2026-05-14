from http.server import HTTPServer, SimpleHTTPRequestHandler

HOST = "localhost"
PORT = 60065  # boobs lol

server = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)

print(f"Serving at http://{HOST}:{PORT}")
server.serve_forever()
