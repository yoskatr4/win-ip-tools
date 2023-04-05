import socket
from http.server import HTTPServer, BaseHTTPRequestHandler

class ProxyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        # Hedef sunucuya bağlanın
        target_host = "thepiratebay.uk.net"
        target_port = 80
        target_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        target_socket.connect((target_host, target_port))

        # Gelen isteği hedef sunucuya iletin
        request_data = "{} {}\r\n".format(self.command, self.path)
        for header, value in self.headers.items():
            request_data += "{}: {}\r\n".format(header, value)
        request_data += "\r\n"
        target_socket.send(request_data.encode())

        # Hedef sunucudan gelen yanıtı geri gönderin
        response_data = target_socket.recv(1024)
        while response_data:
            self.wfile.write(response_data)
            response_data = target_socket.recv(1024)

        # Bağlantıları kapatın
        target_socket.close()
        self.connection.close()

server_address = ('127.0.0.1', 3128)  # proxy sunucusunun IP adresi ve bağlantı noktası
httpd = HTTPServer(server_address, ProxyServer)
print("bağlı")
httpd.serve_forever()
