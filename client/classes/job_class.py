import time
"""
job payload = {
    "id": id,
    "job": job,
}
"""

class Job:
    def __init__(self, payload, max_attempts=3):
        self.payload = payload
        self.attempts = 0
        self.max_attempts = max_attempts
        self.next_run_at = time.time()  # when the job is ready
    
    def to_dict(self):
        return {
            "payload": self.payload,
            "attempts": self.attempts,
            "max_attempts": self.max_attempts,
            "next_run_at": self.next_run_at,
        }