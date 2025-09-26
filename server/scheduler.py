import time, heapq
from datetime import datetime, timedelta
from .classes.job_class import Job

class Scheduler:
    def __init__(self, queue):
        self.queue = queue
        self.jobs = []  # min-heap: (next_run_time, interval_seconds, job content)

    def add_job(self, interval_seconds, job):
        job_obj = Job(job)
        job_dict = job_obj.to_dict()
        next_run = datetime.now() + timedelta(seconds=interval_seconds)
        heapq.heappush(self.jobs, (next_run, interval_seconds, job_dict))

    def run(self):
        while True:
            now = datetime.now()
            if self.jobs and self.jobs[0][0] <= now:
                next_run, interval, job = heapq.heappop(self.jobs)
                self.queue.put(job)  # enqueue for workers
                # re-schedule
                new_time = now + timedelta(seconds=interval)
                heapq.heappush(self.jobs, (new_time, interval, job))
            time.sleep(1)  # check every second