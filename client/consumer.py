from client import run_client, handle_conn
from requests.http_requests import post_user_request, get_root_request, get_hello_request, get_get_job


def run_consumer():
    client_socket = run_client()
    handle_conn(client_socket, "consumer", get_get_job)


if __name__ == "__main__":
    run_consumer()