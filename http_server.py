import http.server
import socketserver

# 指定服务器的地址和端口
HOST = "localhost"
PORT = 8000

# 创建一个简单的HTTP请求处理程序
handler = http.server.SimpleHTTPRequestHandler

# 启动HTTP服务器
with socketserver.TCPServer((HOST, PORT), handler) as server:
    print(f"Server running on http://{HOST}:{PORT}")
    server.serve_forever()