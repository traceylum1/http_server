import json

class Request:
    def __init__(self, method, path, headers, body):
        self.method = method
        self.path = path
        self.headers = headers
        self.body = body
    
    def json(self):
        if self.headers.get("Content-Type") == "application/json":
            return json.loads(self.body or "{}")
        return None