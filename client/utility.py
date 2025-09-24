def parse_http_response(request_data: str):
    lines = request_data.split("\r\n")
    request_line = lines[0]
    version, status_code, status_msg = request_line.split(" ")

    headers = {}
    for line in lines[1:]:
        if line == "":
            break   # end of headers
        key, value = line.split(":", 1)
        headers[key.strip()] = value.strip()
    
    return version, status_code, status_msg, headers