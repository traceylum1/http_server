from queue import Queue
import threading
from .scheduler import Scheduler

max_size = 100
job_queue = Queue(max_size)
results = {}
queue_lock = threading.Lock()

job = {"id": "scheduled_job", "job": "Hello"}
scheduler = Scheduler(job_queue)
scheduler.add_job(10, job)
thread = threading.Thread(target=scheduler.run)
thread.daemon = True  # optional: don’t block exit
thread.start()

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

def results_put(job_id):
    pass

def results_get():
    pass
