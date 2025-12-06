# from queue import Queue
from .scheduler import Scheduler
import threading
import redis
import json

r = redis.Redis(host='localhost', port=6379, decode_responses=True)
max_size = 100
queue_lock = threading.Lock()

# job = {"id": "scheduled_job", "job": "Hello"}
# scheduler = Scheduler(r)
# scheduler.add_job(10, job)
# thread = threading.Thread(target=scheduler.run)
# thread.daemon = True  # optional: don’t block exit
# thread.start()

def enqueue_job(job):
    with queue_lock:
        try:
            r.lpush("queue:jobs", json.dumps(job))
        except Exception as e:
            print(f"Failed to add job to queue.", e)
            raise e

def dequeue_job():
    with queue_lock:
        try:
            job = json.loads(r.lpop("queue:jobs"))
            if not job:
                print("No job available.")
                return None
            return job
        except:
            raise Exception("Failed to get job from queue.")

def results_put(job_id):
    pass

def results_get():
    pass

