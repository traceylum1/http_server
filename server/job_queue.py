# from queue import Queue
from .classes.job_class import Job
import threading
# import redis
import json
from collections import deque


class JobQueue:
    def __init__(self, max_size=100):
        self.max_size = max_size
        self.queue = deque(maxlen=max_size)
        self.queue_lock = threading.Lock()
        self.results = {}

    def enqueue_job(self, job: Job):
        with self.queue_lock:
            self.queue.appendleft(job)

    def dequeue_job(self) -> Job | None:
        with self.queue_lock:
            if self.queue:
                job = self.queue.pop()
                return job
            else:
                print("No job to process.")


# r = redis.Redis(host='localhost', port=6379, decode_responses=True)
# max_size = 100
# queue_lock = threading.Lock()

# job = {"id": "scheduled_job", "job": "Hello"}
# scheduler = Scheduler(r)
# scheduler.add_job(10, job)
# thread = threading.Thread(target=scheduler.run)
# thread.daemon = True  # optional: don’t block exit
# thread.start()

# def enqueue_job(job):
#     with queue_lock:
#         try:
#             r.lpush("queue:jobs", json.dumps(job))
#         except Exception as e:
#             print(f"Failed to add job to queue.", e)
#             raise e

# def dequeue_job():
#     with queue_lock:
#         try:
#             job_json = r.brpoplpush("queue:jobs", "queue:processing", timeout=1)
#             if not job_json:
#                 print("No job available.")
#                 return None
#             return json.loads(job_json)
#         except Exception as e:
#             print("Failed to get job from queue.", e)
#             raise e

# def ack_job(job):
#     r.lrem("queue:processing", 1, json.dumps(job))

# def fail_job(job):
#     job["attempts"] += 1

#     r.lrem("queue:processing", 1, json.dumps(job))

#     if job["attempts"] >= job["max_attempts"]:
#         r.lpush("queue:dead", json.dumps(job))
#     else:
#         r.lpush("queue:jobs", json.dumps(job))


def results_put(job_id):
    pass

def results_get():
    pass

