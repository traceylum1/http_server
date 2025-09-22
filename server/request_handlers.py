
from queue import Queue
from threading import Lock
from .response_builder import response_builder
from client.classes.job_class import Job

max_size = 100
job_queue = Queue(max_size)
results = {}
queue_lock = Lock()


def handle_add_job(job: Job):
    print("Calling handle_add_job...")
    print("job", job)
    payload = job["payload"]
    job_id = payload["id"]
    with queue_lock:
        job_queue.put(payload)
    return response_builder(200, f"Job {job_id} added.")

def handle_get_job():
    print("Calling handle_get_job...")
    job = None
    with queue_lock:
        if job_queue.empty():
            print("No job available.")
            return response_builder(200, "No job")
        job = job_queue.get()
        return response_builder(200, job)
        
def handle_error():
    print("Calling handle_error...")
    return response_builder(404, "Not Found")




# def handle_root():
#     print("Calling handle_root...")
#     return response_builder(200, "Hello, world!")

# def handle_hello():
#     print("Calling handle_hello...")
#     return response_builder(200, "Hello, there!")

# def handle_user(body_data):
#     print("Calling handle_user...")
#     print("body_data", body_data)
#     user_id = body_data.get("id") if body_data else None
#     user_data = {"id": user_id, "name": "Abe"}

#     return response_builder(200, user_data)
