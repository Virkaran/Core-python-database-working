import http.server
import socketserver

PORT = 8001

Handler = http.server.SimpleHTTPRequestHandler

http_server = socketserver.TCPServer(("", PORT), Handler)

print ("port is:", PORT)
http_server.serve_forever()