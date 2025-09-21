from request import Request
import json
from utility import parse_uri
from queue import Queue
from threading import Lock

max_size = 100
job_queue = Queue(max_size)
results = {}
queue_lock = Lock()


def build_response(status_code: int, body: str):
    reason_phrases = {
        200: "OK",
        201: "Created",
        400: "Bad Request",
        404: "Not Found",
        405: "Method Not Allowed",
    }
    reason = reason_phrases.get(status_code, "Unknown")

    body_bytes = json.dumps(body).encode("utf-8")
    return (
        f"HTTP/1.1 {status_code} {reason}\r\n"
        f"Content-Length: {len(body_bytes)}\r\n"
        "Content-Type: text/plain\r\n"
        "\r\n"
    ).encode("utf-8") + body_bytes


def handle_request(request: Request):
    method = request.method
    resource, params, query_params = parse_uri(request.path)

    # Decision logic
    if resource == "" and method == "GET":
        return handle_root()
    elif resource == "hello" and method == "GET":
        return handle_hello()
    elif resource == "user" and method == "POST":
        body_data = request.json()
        return handle_user(body_data)
    elif resource == "add_job" and method == "POST":
        body = request.json()
        return handle_add_job(body)
    elif resource == "get_job" and method == "GET":
        return handle_get_job()
    else:
        return build_response(404, "")
    

def handle_root():
    print("Calling handle_root...")
    return build_response(200, "Hello, world!")

def handle_hello():
    print("Calling handle_hello...")
    return build_response(200, "Hello, there!")

def handle_user(body_data):
    print("Calling handle_user...")
    print("body_data", body_data)
    user_id = body_data.get("id") if body_data else None
    user_data = {"id": user_id, "name": "Abe"}

    return build_response(200, user_data)

def handle_add_job(job):
    print("Calling handle_add_job...")
    job_id = job.get("job_id")
    with queue_lock:
        job_queue.put(job)
    return build_response(200, f"Job {job_id} added.")

def handle_get_job():
    print("Calling handle_get_job...")
    job_id = None
    with queue_lock:
        if job_queue.empty():
            print("No job available.")
            return build_response(200, "No job")
        job_id = job_queue.get()
        return build_response(200, job_id)
        

# ROUTES = {
#     ("GET", "/"): handle_root,
#     ("GET", "/hello"): handle_hello,
#     ("POST", "/user"): handle_user,
# }