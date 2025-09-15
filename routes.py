from request import Request
import json

def handle_root(request: Request):
    print("Calling handle_root")
    return "HTTP/1.1 200 OK\r\nContent-Length: 13\r\n\r\nHello, world!".encode("utf-8")

def handle_hello(request: Request):
    print("Calling handle_hello")
    return "HTTP/1.1 200 OK\r\nContent-Length: 12\r\n\r\nHello there!".encode("utf-8")

def handle_user(request: Request):
    print("Calling handle_user")
    data = request.json()
    print("data", data)
    user_id = data.get("id") if data else None
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