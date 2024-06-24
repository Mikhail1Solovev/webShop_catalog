from http.server import BaseHTTPRequestHandler, HTTPServer

host_name = "localhost"
server_port = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        with open("index.html", "r", encoding="utf-8") as file:
            self.wfile.write(bytes(file.read(), "utf-8"))

if __name__ == "__main__":
    web_server = HTTPServer((host_name, server_port), MyServer)
    print(f"Server started http://{host_name}:{server_port}")

    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass

    web_server.server_close()
    print("Server stopped.")
