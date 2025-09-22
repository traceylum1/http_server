from .client import run_client, handle_conn
from .requests.http_requests import *

def run_consumer():
    client_socket = run_client()
    handle_conn(client_socket, "consumer", get_get_job)


if __name__ == "__main__":
    run_consumer()