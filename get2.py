from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver
import http.server

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type','text/html')
        self.end_headers()
        output=''
        output+='<html><body>'
        output+='<form method="POST" action="/get2">'
        output+='name: <input type="text" id="name">'
        output+='<input type="submit" value="submit">'
        output+='</form>'
        output+='</body></html>'

        self.wfile.write(output.encode())

    # def do_POST(self): 
    #     if self.path.endswith('/get2'):
    #         ctype,pdict=cgi.parse_header(self.headers.get('content-type'))
    #         pdict['boundary']=bytes(pdict['boundary'],"UTF-8")
    #         # content-len
    #         # if ctype='multipart/form-data':
    #         #     resopnse=cgi.parse_multipart(self.rfile.pdict)

    #         self.send_response(200)
    #         # self.send_headers('content-type','text/html')
    #         # self.send_headers('Location','/get2')
    #         self.wfile.write(b'<html><body>POST response</body></html>')
    #         self.end_headers()
       



def main():
    PORT = 8001
    Handler = http.server.SimpleHTTPRequestHandler
    http_server = socketserver.TCPServer(("", PORT), Handler)
    print ("port is:", PORT)
    http_server.serve_forever()
if __name__=='__main__':
    main()