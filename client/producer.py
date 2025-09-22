from .client import run_client, handle_conn
from .requests.http_requests import *


def run_producer():
    client_socket = run_client()
    handle_conn(client_socket, "producer", post_add_job)


if __name__ == "__main__":
    run_producer()