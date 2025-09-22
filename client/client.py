import socket

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
                # Call job handler
                pass

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
