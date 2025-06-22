'''
Functions for:
-Logging
-Latency modeling (e.g., random delay functions)
-Data formatting
-Result export to DataFrame
'''

import random

def log_event(env, message):
    """adds readable timestamps to your print logs for debugging and storytelling"""
    print(f"[{env.now:.4f}s] {message}")

def simulate_latency(latency_ms):
    return latency_ms / 1000.0

def add_jitter(base_latency, jitter_range=5):
    jitter = random.uniform(-jitter_range, jitter_range)
    return max(0.0, base_latency + jitter)
