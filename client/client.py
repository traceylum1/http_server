import socket
from http_requests import post_user_request, get_root_request, get_hello_request

def handle_conn(client_socket):
    print("Sending request...")
    try:
        get_hello_request(client_socket)
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
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        host = 'localhost'
        port = 8000

        client_socket.connect((host, port))
        print("Client connected")
        handle_conn(client_socket)


if __name__ == "__main__":
    run_client()

# total_bytes_sent = 0
# while total_bytes_sent < len(body_bytes):
#     bytes_sent = client_socket.send(http_request)
#     total_bytes_sent += bytes_sent
#     print(f"Sent {bytes_sent} bytes")