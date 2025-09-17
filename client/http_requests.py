import socket

def request_builder(method, uri, body=None):
    body_bytes = body.encode("utf-8") if body != None else "".encode("utf-8")
    content_type = "application/json" if method=="POST" else "text/plain"
    return (
        f"{method} {uri} HTTP/1.1\r\n"
        f"Host: localhost\r\n"
        f"Content-Type: {content_type}\r\n"
        f"Content-Length: {len(body_bytes)}\r\n"
        f"Connection: close \r\n\r\n"
        ).encode("utf-8") + body_bytes


def post_user_request(socket: socket):
    print("Calling post_user_request...")
    body = '{"id": "123"}'
    http_request = request_builder("POST", "/user", body)
    socket.sendall(http_request)
    return

def get_root_request(socket: socket):
    print("Calling get_root_request...")
    http_request = request_builder("GET", "/")
    socket.sendall(http_request)
    return

def get_hello_request(socket: socket):
    print("Calling get_hello_request")
    http_request = request_builder("GET", "/hello")
    socket.sendall(http_request)
    return