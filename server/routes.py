from request import Request
import json
from utility import parse_uri
from request_handlers import *


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
        return handle_error()