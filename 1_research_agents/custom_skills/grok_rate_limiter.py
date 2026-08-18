import time

class GrokRateLimiter:
    def __init__(self, max_calls_per_min=60):
        self.interval = 60.0 / max_calls_per_min
        self.last_call = 0.0

    def wait(self):
        elapsed = time.time() - self.last_call
        if elapsed < self.interval:
            time.sleep(self.interval - elapsed)
        self.last_call = time.time()
