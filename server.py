import SimpleHTTPServer
import SocketServer
import argparse
 
class MyRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
       	self.protocol_version='HTTP/1.1'
       	self.send_response(200, 'OK')
       	self.send_header('Content-type', 'text/html')
       	self.end_headers()
       	self.wfile.write("OK")
    	return

parser = argparse.ArgumentParser(description='HTTP Server')
parser.add_argument('port', type=int, help='Listening port for HTTP Server')
args = parser.parse_args()

Handler = MyRequestHandler
server = SocketServer.TCPServer(('0.0.0.0', args.port), Handler)
print 'HTTP Server Running...........'

server.serve_forever()
