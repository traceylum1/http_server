from urllib.parse import urlparse, parse_qs

def parse_uri(uri: str):
    """
    Break a URI into resource, path params, and query params.
    """
    parsed = urlparse(uri)

    # Path: "/users/123" → ["users", "123"]
    path_parts = [p for p in parsed.path.split("/") if p]

    resource = path_parts[0] if path_parts else None
    params = path_parts[1:]  # everything after the resource

    # Query string: "?postId=42&limit=10" → {"postId": ["42"], "limit": ["10"]}
    query_params = parse_qs(parsed.query)

    # Flatten query values (["42"] → "42") for convenience
    query_params = {k: v[0] if len(v) == 1 else v for k, v in query_params.items()}

    return resource, params, query_params


def parse_http_request(request_data: str):
    lines = request_data.split("\r\n")
    request_line = lines[0]
    method, path, version = request_line.split(" ")

    headers = {}
    for line in lines[1:]:
        if line == "":
            break   # end of headers
        key, value = line.split(":", 1)
        headers[key.strip()] = value.strip()
    
    return method, path, version, headers