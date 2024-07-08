from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/json')
        self.end_headers()

        message = "{'Hello': 'World!'}"
        self.wfile.write(bytes(message, "utf8"))    # respuesta enviada del servidor

    def do_POST(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()

        message = "Hello, World! Here is POST response"
        self.wfile.write(bytes(message, "utf8"))

# with HTTPServer(('', 8000), handler) as server:
#     server.serve_forever()

try:

    print(1)

except:

    print(2)

finally:

    print(3)