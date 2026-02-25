import time, heapq
from datetime import datetime, timedelta
from .classes.job_class import Job
from .job_queue import JobQueue

class Scheduler:
    def __init__(self, queue: JobQueue):
        self.queue = queue
        self.scheduled_jobs = []  # min-heap: (next_run_time, interval_seconds, job content)

    def add_job(self, interval_seconds, job):
        job_obj = Job(job)
        job_dict = job_obj.to_dict()
        next_run = datetime.now() + timedelta(seconds=interval_seconds)
        heapq.heappush(self.scheduled_jobs, (next_run, interval_seconds, job_dict))

    def run(self):
        while True:
            now = datetime.now()
            if self.scheduled_jobs and self.scheduled_jobs[0][0] <= now:
                next_run, interval, job = heapq.heappop(self.scheduled_jobs)
                self.queue.enqueue_job(job)  # enqueue for workers
                # re-schedule
                new_time = now + timedelta(seconds=interval)
                heapq.heappush(self.scheduled_jobs, (new_time, interval, job))
            time.sleep(1)  # check every second