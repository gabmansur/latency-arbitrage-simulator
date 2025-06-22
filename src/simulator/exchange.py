import simpy
import random
from src.simulator.utils import log_event

class Exchange:
    def __init__(self, env, name, base_price=100.0, jitter=0.5, update_interval=0.2):
        self.env = env
        self.name = name
        self.price = base_price
        self.jitter = jitter
        self.update_interval = update_interval

        self.env.process(self.simulate_price_changes())

    def simulate_price_changes(self):
        while True:
            change = random.uniform(-self.jitter, self.jitter)
            self.price += change
            self.price = max(0.01, self.price)
            log_event(self.env, f"[{self.name}] New price: ${self.price:.2f}")
            yield self.env.timeout(self.update_interval)