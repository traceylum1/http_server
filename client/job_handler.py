from .classes.job_class import Job, Payload
import random

"""
job payload = {
    "id": id,
    "job": job,
}
"""
# Backoff calculation (exponential + jitter)
def backoff_delay(attempt, base=1, cap=30):
    delay = min(base * (2 ** (attempt - 1)), cap)
    jitter = random.uniform(0, delay * 0.1)  # ±10%
    return delay + jitter


def job_handler(job: Job):
    payload: Payload = job.payload
    job_id = payload.id
    job_content = payload.content

    now = time.time()

    # Wait until it's time to run this job
    if job.next_run_at > now:
        job_queue.put(job)
        time.sleep(0.1)
        continue
