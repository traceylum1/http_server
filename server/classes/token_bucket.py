"""
Token bucket class:
    - Holds a certain number of tokens at any given time
    - Tokens refill at a given pace (tokens per second)
    - A
"""

import time

class Token_Bucket:
    def __init__(self, capacity, pace):
        self.capacity = capacity
        self.pace_to_add = pace     # tokens/second
        self.tokens = capacity
        self.last_added = time.time()
    
    """
        add_tokens checks if capacity is full, if not, adds however many tokens as needed since last time added
        time_elapsed = now - last_added
        tokens_to_add = time_elapsed * pace_to_add
    """
    def add_tokens(self):
        print("Calling add_tokens...")
        if self.tokens < self.capacity:
            time_elapsed = int(time.time() - self.last_added)
            tokens_to_add = self.pace_to_add * time_elapsed
            prelim_token_count = self.tokens + tokens_to_add
            tokens_over_capacity = prelim_token_count - self.capacity
            if tokens_over_capacity > 0:
                tokens_to_add -= tokens_over_capacity
            print(f"Adding {tokens_to_add} tokens")
            self.tokens += tokens_to_add
            
            if self.tokens > self.capacity:
                self.tokens = self.capacity
            print("Current number of tokens: ", self.tokens)
            self.last_added = time.time()

    """
        use_token removes one token from token bucket per request received if available
        returns True if token available, False otherwise
    """
    def use_token(self):
        print("Calling use_token...")
        if self.tokens == 0:
            print("No tokens available, please wait and try again")
            return False
        else:
            print("Using a token")
            self.tokens -= 1
            return True

    """
        run the token_bucket, calling add_tokens in an infinite loop
    """
    def run(self):
        while True:
            self.add_tokens()
            time.sleep(5)