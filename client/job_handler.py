import time
import random
import json

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

# Example "work" function
def do_work():
    if random.random() < 0.7:  # 70% chance to fail
        raise Exception("Simulated failure")
    time.sleep(1)  # simulate processing time


def job_handler(job):
    job_dict = json.loads(job)
    payload = job_dict["payload"]
    job_id = payload["id"]

    while True:
        now = time.time()
        # Wait until it's time to run this job
        if job_dict["next_run_at"] > now:
            time.sleep(1)
            continue
        try:
            print(f"Processing job {job_id}, attempt {job_dict['attempts'] + 1}")
            do_work()
            print(f"Job {job_id} completed")
            break
        except Exception as e:
            job_dict["attempts"] += 1
            if job_dict["attempts"] < job_dict["max_attempts"]:
                delay = backoff_delay(job_dict["attempts"])
                job_dict["next_run_at"] = time.time() + delay
                print(f"Job {job_id} failed ({e}), retrying in {delay:.2f}s...")
            else:
                print(f"Job {job_id} permanently failed after {job_dict['attempts']} attempts")
                break