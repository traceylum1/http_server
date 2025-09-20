from request import Request
import json
from utility import parse_uri

http_status_codes = {
    # 2xx Success
    200: "OK",
    201: "Created",
    204: "No Content",

    # 3xx Redirection
    301: "Moved Permanently",
    302: "Found",
    304: "Not Modified",

    # 4xx Client Errors
    400: "Bad Request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Not Found",
    405: "Method Not Allowed",
    429: "Too Many Requests",

    # 5xx Server Errors
    500: "Internal Server Error",
    502: "Bad Gateway",
    503: "Service Unavailable",
    504: "Gateway Timeout",
}


def build_response(status_code: int, body: str):
    reason_phrases = {
        200: "OK",
        201: "Created",
        400: "Bad Request",
        404: "Not Found",
        405: "Method Not Allowed",
    }
    reason = reason_phrases.get(status_code, "Unknown")

    body_bytes = body.encode("utf-8")
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

    body_bytes = json.dumps(user_data)
    return build_response(200, body_bytes)

ROUTES = {
    ("GET", "/"): handle_root,
    ("GET", "/hello"): handle_hello,
    ("POST", "/user"): handle_user,
}