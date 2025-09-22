from .request_builder import request_builder
import uuid
import json
from ..classes.job_class import Job

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
    print("Calling post_add_job...")
    job_id = str(uuid.uuid4())[:8]
    job_content = "Hello"

    payload = {
        "id": job_id,
        "job": job_content,
    }

    job = Job(payload)
    job_dict = job.to_dict()
    return request_builder("POST", "/add_job", json.dumps(job_dict))

def get_get_job():
    print("Calling get_get_job...")
    return request_builder("GET", "/get_job")