import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

msg = 'hello'

host = 'localhost'
port = 8000

client_socket.connect((host, port))
print("Client connected")

msg = "Hello, server!"
msg_len = len(msg)
http_request = f"POST / HTTP/1.1\r\n" \
    "Host: localhost\r\n" \
    "Content-Type: text/plain\r\n" \
    f"Content-Length: {str(msg_len)}\r\n" \
    "Connection: close \r\n\r\n" \
    f"{msg}"

total_bytes_sent = 0
while total_bytes_sent < msg_len:
    bytes_sent = client_socket.send(http_request.encode('utf-8'))
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