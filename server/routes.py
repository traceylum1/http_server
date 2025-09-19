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


def response_builder(request: Request):
    method = request.method
    path = request.path
    resource, params, query_params = parse_uri(path)
    
    return (
        "HTTP/1.1 404 Not Found\r\n"
        "Content-Length: 9\r\n"
        "Content-Type: text/plain\r\n"
        "\r\n"
        "Not Found"
    ).encode("utf-8")

    

def handle_root(request: Request):
    print("Calling handle_root...")
    return "HTTP/1.1 200 OK\r\nContent-Length: 13\r\n\r\nHello, world!".encode("utf-8")

def handle_hello(request: Request):
    print("Calling handle_hello...")
    return "HTTP/1.1 200 OK\r\nContent-Length: 12\r\n\r\nHello there!".encode("utf-8")

def handle_user(request: Request):
    print("Calling handle_user...")
    body_data = request.json()
    print("body_data", body_data)
    user_id = body_data.get("id") if body_data else None
    user_data = {"id": user_id, "name": "Abe"}

    body_bytes = json.dumps(user_data).encode("utf-8")
    return (
        "HTTP/1.1 200 OK\r\n"
        f"Content-Length: {len(body_bytes)}\r\n"
        "Content-Type: application/json\r\n"
        "\r\n"
    ).encode() + body_bytes

ROUTES = {
    ("GET", "/"): handle_root,
    ("GET", "/hello"): handle_hello,
    ("POST", "/user"): handle_user,
}