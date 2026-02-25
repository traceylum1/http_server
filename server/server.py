import socket
from .utility import parse_http_request
from .routes import handle_request
from .classes.request_class import Request
import threading
from .classes.token_bucket import TokenBucket
from .response_builder import response_builder

def handle_client(client_socket: socket, address, limiter: TokenBucket):
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

                # Reading headers before using rate limiter allows for more control
                # Avoids wasting resources reading body if not necessary
                if limiter.use_token() == False:
                    response = response_builder(429, "Too Many Requests")
                    client_socket.sendall(response)
                    break

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

                # Send response back to client
                try:
                    # handler = ROUTES.get((method, path))
                    request = Request(method, path, headers, body)
                    response = handle_request(request)

                    client_socket.sendall(response)

                except Exception as e:
                    print(f"Error sending response: {e}")
                
                finally:
                    print("Finished handling client request.")
                    break


def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        host = 'localhost'
        port = 8000

        server_socket.bind((host, port))
        server_socket.listen(5)
        print("Server listening on localhost port 8000")

        limiter = TokenBucket(1, 1)

        while True:
            
            # Wait for client to connect to socket
            try:
                client_socket, address = server_socket.accept()
                print("Opened client socket")
                # Spawn a new thread for each client
                thread = threading.Thread(target=handle_client, args=(client_socket, address, limiter))
                thread.daemon = True  # optional: don’t block exit
                thread.start()

            except OSError as e:
                print(f"Client socket error: {e}")
                break

if __name__ == "__main__":
    import signal
    import sys
    from .job_queue import r   # whatever file holds it

    def shutdown_handler(signum, frame):
        print("Shutting down HTTP server...")

        # Close Redis
        r.close()
        print("Closed Redis connection.")

        # Optionally wait for worker threads to finish
        sys.exit(0)

    signal.signal(signal.SIGINT, shutdown_handler)
    signal.signal(signal.SIGTERM, shutdown_handler)

    run_server()
