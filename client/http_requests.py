import socket
from request_builder import request_builder

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