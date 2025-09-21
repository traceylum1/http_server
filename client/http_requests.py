import socket
from request_builder import request_builder
import uuid
import json

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

def post_add_job(socket: socket):
    print("Calling get_add_job...")
    job_id = str(uuid.uuid4())[:8]
    jobObj = {
        "job_id": job_id,
        "job": "Hello"
    }
    http_request = request_builder("POST", "/add_job", json.dumps(jobObj))
    socket.sendall(http_request)
    return

def get_get_job(socket: socket):
    print("Calling get_get_job...")
    http_request = request_builder("GET", "/get_job")
    socket.sendall(http_request)
    return