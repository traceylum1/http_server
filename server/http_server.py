import socket
from utility import parse_http_request
from routes import ROUTES
from request import Request
import threading

def handle_client(client_socket, address):
    with client_socket:
        # Receive all data from client, store in buffer
        buffer = ""
        while True:
            data = client_socket.recv(1024).decode("utf-8")
            if not data:
                print("Connection closed unexpectedly")
                break
            buffer += data

            # Check for end of headers
            if "\r\n\r\n" in buffer:
                print("Full header received")
                print(buffer)
                header_part, body_part = buffer.split("\r\n\r\n")
                method, path, version, headers = parse_http_request(header_part)

                # If POST or PUT request, make sure full body received
                body = body_part
                if method == "POST" or method == "PUT":
                    print("Receive body for POST or PUT")
                    content_length = int(headers.get("Content-Length", 0))

                    while len(body) < content_length:
                        body_data = client_socket.recv(1024).decode("utf-8")
                        if not data:
                            print("Connection closed unexpectedly")
                            break
                        body += body_data
                    print("Body: ", body)

                # Send response back to client
                try:
                    handler = ROUTES.get((method, path))
                    request = Request(method, path, headers, body)
                    response = None

                    if handler:
                        response = handler(request)
                    else:
                        response = (
                            "HTTP/1.1 404 Not Found\r\n"
                            "Content-Length: 9\r\n"
                            "Content-Type: text/plain\r\n"
                            "\r\n"
                            "Not Found"
                        ).encode("utf-8")

                    client_socket.sendall(response)

                except Exception as e:
                    print(f"Error sending response: {e}")
                
                finally:
                    print("Finished handling client.")
                    break


def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        host = 'localhost'
        port = 8000

        server_socket.bind((host, port))
        server_socket.listen(5)

        while True:
            print("Server listening on localhost port 8000")
            # Wait for client to connect to socket
            try:
                client_socket, address = server_socket.accept()
                print("Opened client socket")
                # Spawn a new thread for each client
                thread = threading.Thread(target=handle_client, args=(client_socket, address))
                thread.daemon = True  # optional: don’t block exit
                thread.start()

            except OSError as e:
                print(f"Client socket error: {e}")
                break

if __name__ == "__main__":
    run_server()

                    # print("Sending response...")
                    # msg = "Hello, client!"
                    # msg_len = len(msg)
                    # http_response = f"HTTP/1.1 200 OK\r\n" \
                    #     "Content-Type: text/plain\r\n" \
                    #     f"Content-Length: {str(msg_len)}\r\n" \
                    #     "Connection: close\r\n\r\n" \
                    #     f"{msg}"

                    # total_bytes_sent = 0
                    # while total_bytes_sent < len(http_response):
                    #     bytes_sent = client_socket.send(http_response.encode('utf-8'))
                    #     print(f"Sent {bytes_sent} bytes")
                    #     total_bytes_sent += bytes_sent