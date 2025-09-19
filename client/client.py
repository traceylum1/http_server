import socket
from http_requests import post_user_request, get_root_request, get_hello_request

def handle_conn(client_socket, handle_request):
    print("Sending request...")
    with client_socket:
        try:
            handle_request(client_socket)
            buffer = ""
            while True:
                data = client_socket.recv(1024).decode("utf-8")
                if not data:
                    break
                buffer += data

                if "\r\n\r\n" in buffer:
                    print("Full header received")
                    print(buffer)

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
