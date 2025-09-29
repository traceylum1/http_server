"""
Token bucket class:
    - Holds a certain number of tokens at any given time
    - Tokens refill at a given pace (tokens per second)
"""

import time
from threading import Lock

class TokenBucket:
    def __init__(self, capacity: int, refill_rate: int):
        """
        :param capacity: max number of tokens in the bucket
        :param refill_rate: tokens added per second
        """
        self.capacity = capacity
        self.tokens = capacity
        self.refill_rate = refill_rate
        self.last_added = time.time()
        self.lock = Lock()
    
    """
        refill_tokens adds however many tokens as needed since last time added
    """
    def refill_tokens(self):
        print("Calling refill_tokens...")
        now = time.time()
        time_elapsed = int(now - self.last_added)
        tokens_to_add = self.refill_rate * time_elapsed
        if tokens_to_add > 0:
            prelim_token_count = self.tokens + tokens_to_add
            self.tokens = min(prelim_token_count, self.capacity)
            print("Current number of tokens: ", self.tokens)
            self.last_added = now

    """
        use_token calls refill_tokens and removes one token from token bucket per request received if available
        returns True if token available, False otherwise
    """
    def use_token(self) -> bool:
        print("Calling use_token...")
        with self.lock:
            self.refill_tokens()
            if self.tokens >= 1:
                print("Using a token")
                self.tokens -= 1
                return True
            print("No tokens available")
            return False
