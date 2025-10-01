import time
from collections import deque
from threading import Lock

class SlidingWindowLimiter:
    def __init__(self, max_requests: int, window_size: float):
        """
        :param max_requests: max requests allowed per window
        :param window_size: window size in seconds
        """
        self.max_requests = max_requests
        self.window_size = window_size
        self.requests = deque()
        self.lock = Lock()

    def allow_request(self) -> bool:
        now = time.time()
        with self.lock:
            # Remove old requests outside the window
            while self.requests and self.requests[0] <= now - self.window_size:
                self.requests.popleft()

            if len(self.requests) < self.max_requests:
                self.requests.append(now)
                return True
            else:
                return False