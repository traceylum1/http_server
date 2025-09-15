import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 8000

client_socket.connect((host, port))
print("Client connected")

body = '{"id": "123"}'
body_bytes = body.encode("utf-8")

http_request = (
    "POST /user HTTP/1.1\r\n"
    "Host: localhost\r\n"
    "Content-Type: application/json\r\n"
    f"Content-Length: {len(body_bytes)}\r\n"
    "Connection: close \r\n\r\n"
    ).encode("utf-8") + body_bytes

total_bytes_sent = 0
while total_bytes_sent < len(body_bytes):
    bytes_sent = client_socket.send(http_request)
    total_bytes_sent += bytes_sent
    print(f"Sent {bytes_sent} bytes")

buffer = ""
while True:
    data = client_socket.recv(1024).decode("utf-8")
    if not data:
        break
    buffer += data

    if "\r\n\r\n" in buffer:
        print("Full header received")
        print(buffer)


client_socket.close()