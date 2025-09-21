import socket
from requests.request_builder import request_builder
import uuid
import json

def post_user_request():
    print("Calling post_user_request...")
    body = '{"id": "123"}'
    return request_builder("POST", "/user", body)

def get_root_request():
    print("Calling get_root_request...")
    return request_builder("GET", "/")
    

def get_hello_request():
    print("Calling get_hello_request")
    return request_builder("GET", "/hello")

def post_add_job():
    print("Calling get_add_job...")
    job_id = str(uuid.uuid4())[:8]
    jobObj = {
        "job_id": job_id,
        "job": "Hello"
    }
    return request_builder("POST", "/add_job", json.dumps(jobObj))

def get_get_job():
    print("Calling get_get_job...")
    return request_builder("GET", "/get_job")