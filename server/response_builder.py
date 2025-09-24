import json

def response_builder(status_code: int, body: str, content: str):
    reason_phrases = {
        200: "OK",
        201: "Created",
        400: "Bad Request",
        404: "Not Found",
        405: "Method Not Allowed",
    }
    reason = reason_phrases.get(status_code, "Unknown")
    content_type = "application/json" if content == "json" else "text/plain"

    body_bytes = json.dumps(body).encode("utf-8") if content == "json" else body.encode("utf-8")
    return (
        f"HTTP/1.1 {status_code} {reason}\r\n"
        f"Content-Length: {len(body_bytes)}\r\n"
        f"Content-Type: {content_type}\r\n"
        "\r\n"
    ).encode("utf-8") + body_bytes

