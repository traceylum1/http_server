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