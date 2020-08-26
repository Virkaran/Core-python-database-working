from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver
import http.server
import cgi

info = []
class requesthandler(BaseHTTPRequestHandler):
    def do_GET(self):
      if self.path.endswith('/form'):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        output = ''
        output += '<html><body>'
        output += '<h1>User and Book list</h1>'
        for i in info:
            output +=i
            output += '</br>'
        output += '</body></html>'
        self.wfile.write(output.encode())
    
      if self.path.endswith('/newuser'):
          self.send_response(200)
          self.send_header('content-type', 'text/html')
          self.end_headers()
          output = ''
          output += '<html><body>'
          output += '<h1>Add New User</h1>'
          output += '<form method="POST" enctype="multipart/form-data" action="/form/newuser">'
          output += 'USER: <input name="task" type="text" palceholder="User Name ">'
          output += '</br>'
          output += '<input type ="submit" value="Add">'
          output += '</form>'
          output += '</body></html>'
          self.wfile.write(output.encode())
      
    #   if self.path.endswith('/book'):
    #       self.send_response(200)
    #       self.send_header('content-type', 'text/html')
    #       self.end_headers()
    #       output = ''
    #       output += '<html><body>'
    #       output += '<h1>Add new book</h1>'
    #       output += '<form method="POST" enctype="multipart/form-data" action="/form/book">'
    #       output += '<input name="task" type="text" palceholder="Book Name">'
    #       output += '<input type ="submit" value="Add">'
    #       output += '</form>'
    #       output += '</body></html>'
    #       self.wfile.write(output.encode())

    def do_POST(self):

        # if self.path.endswith('/book'):
        #     self.send_response(200)
        #     self.send_header('content-type','text/html')
        #     self.end_headers()
        #     output=''
        #     output+='<html><body>'
        #     output+='<h1>ADD-BOOKS</h1>'
        #     output+='<form method="POST" enctype="multipart/form-data" action="/form/book">'
        #     output+='<input type="text" name="task" >'
        #     output+='<input type="submit value="add">'
        #     output+='</form>'
        #     output+='</body></html>'

        #     self.wfile.write(output.encode())   

        if self.path.endswith('/newuser'):
             ctype,pdict =cgi.parse_header(self.headers.get('content-type'))
             pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
             content_len = int(self.headers.get('Content-length'))
             pdict['CONTENT-LENGTH'] = content_len
             if ctype == 'multipart/form-data':
                 fields =cgi.parse_multipart(self.rfile,pdict)
                 new_task=fields.get('task')
                 info.append(new_task[0])
             self.send_response(200)
             self.send_header('content-type','text/html')
             self.send_header('location','/form')
             self.end_headers() 
        
        # f=open(data.json)
        # data=json.dumps(info)



        # if self.path.endswith('/book'):
        #      ctype,pdict =cgi.parse_header(self.headers.get('content-type'))
        #      pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
        #      content_len = int(self.headers.get('Content-length'))
        #      pdict['CONTENT-LENGTH'] = content_len
        #      if ctype == 'multipart/form-data':
        #          fields =cgi.parse_multipart(self.rfile,pdict)
        #          new_task=fields.get('task')
        #          info.append(new_task[0])
        #      self.send_response(200)
        #      self.send_header('content-type','text/html')
        #      self.send_header('location','/form')
        #      self.end_headers()       

def main():
    PORT = 8001
    server_address=('localhost',PORT)
    server=HTTPServer(server_address,requesthandler)
    print ("port is:", PORT)
    server.serve_forever()

if __name__=='__main__':
    main()
