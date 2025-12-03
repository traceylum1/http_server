from queue import Queue
from .scheduler import Scheduler
import threading


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


# import redis

# def run_queue():
#     r = redis.Redis(host='localhost', port=6379, decode_responses=True)

#     r.set('foo', 'bar')
#     # True
#     r.get('foo')
#     # bar

#     r.hset('user-session:123', mapping={
#         'name': 'John',
#         "surname": 'Smith',
#         "company": 'Redis',
#         "age": 29
#     })
#     # True

#     r.hgetall('user-session:123')
#     # {'surname': 'Smith', 'name': 'John', 'company': 'Redis', 'age': '29'}

#     r.close()


# if __name__ == "__main__":
#     run_queue()