import socket
from .job_handler import job_handler
from .utility import parse_http_response

def handle_conn(client_socket, client_type, create_request):
    print("Sending request...")
    with client_socket:
        try:
            http_request = create_request()
            client_socket.sendall(http_request)
            buffer = ""
            while True:
                data = client_socket.recv(1024).decode("utf-8")
                if not data:
                    break
                buffer += data

                if "\r\n\r\n" in buffer:
                    print("Full header received")
                    print(buffer)
                
                    if client_type == "consumer":
                        header_part, body_part = buffer.split("\r\n\r\n")
                        version, status_code, status_msg, headers = parse_http_response(header_part)
                        if status_code != "200":
                            print(f"Response returned: {status_code} {status_msg}")
                            break

                        body = body_part
                        content_length = int(headers.get("Content-Length", 0))

                        while len(body) < content_length:
                            body_data = client_socket.recv(1024).decode("utf-8")
                            if not data:
                                print("Connection closed unexpectedly")
                                break
                            body += body_data
                        if body == "No job":
                            print("Nothing to process.")
                            return
                        else:
                            try:
                                # Call job handler
                                job_handler(body)
                            except Exception as e:
                                print(f"Error processing job: {e}")

        except Exception as e:
            print(f"Error sending request: {e}")
        

def run_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'localhost'
    port = 8000

    client_socket.connect((host, port))
    print("Client connected")
    return client_socket


if __name__ == "__main__":
    run_client()
