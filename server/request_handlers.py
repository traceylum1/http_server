from .response_builder import response_builder
from .job_queue import enqueue_job, dequeue_job

def handle_add_job(job):
    print("Calling handle_add_job...")
    payload = job["payload"]
    job_id = payload["id"]
    try:
        enqueue_job(job)
    except Exception as e:
        print(f"Error: {e}")
        return response_builder(500, f"{e} Job ID: {job_id}")
    return response_builder(200, f"Job {job_id} added.")

def handle_get_job():
    print("Calling handle_get_job...")
    job = None
    try:
        job = dequeue_job()
        if job == None:
            return response_builder(200, "No job")
        return response_builder(200, job)
    except Exception as e:
        print(f"Error: {e}")
        
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
