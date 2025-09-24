
from queue import Queue
from threading import Lock

max_size = 100
job_queue = Queue(max_size)
results = {}
queue_lock = Lock()

def enqueue_job(job):
    with queue_lock:
        try:
            job_queue.put(job)
        except:
            raise Exception("Failed to add job to queue.")

def dequeue_job():
    with queue_lock:
        try:
            if job_queue.empty():
                print("No job available.")
                return None
            return job_queue.get()
        except:
            raise Exception("Failed to get job from queue.")
