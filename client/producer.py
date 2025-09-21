from client import run_client, handle_conn
from http_requests import post_user_request, get_root_request, get_hello_request, post_add_job


def run_producer():
    client_socket = run_client()
    handle_conn(client_socket, post_add_job)


if __name__ == "__main__":
    run_producer()