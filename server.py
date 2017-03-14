from http import server
import socketserver
from urllib.parse import urlparse, parse_qs


class StreamingHandler(server.BaseHTTPRequestHandler):
    def do_GET(self):
        url = urlparse(self.path)
        if url.path != '/':
            self.send_response(200)
            self.end_headers()
            return
        query = parse_qs(url.query)
        direction = query['direction'][0]
        side = query['side'][0]
        enabled = query['enabled'][0] == 'true'
        speed = int(query['speed'][0])
        content = 'direction: {}\n'\
            'side: {}\n'\
            'enabled: {}\n'\
            'speed: {}'.format(direction, side, enabled, speed).encode('utf-8')
        self.send_response(200)
        self.send_header('Age', 0)
        self.send_header('Cache-Control', 'no-cache, private')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(content))
        self.end_headers()
        self.wfile.write(content)


class StreamingServer(socketserver.ThreadingMixIn, server.HTTPServer):
    allow_reuse_address = True
    daemon_threads = True


address = ('0.0.0.0', 8000)
server = StreamingServer(address, StreamingHandler)
server.serve_forever()
