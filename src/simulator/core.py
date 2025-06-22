''' 
-Initializes the SimPy environment.
-Simulates the exchanges with artificial latency.
-Creates and manages agents.
-Orchestrates the flow of orders, market updates, and trades.
-Logs trade executions and latencies.
'''

import simpy
from src.simulator.utils import log_event
from simulator.exchange import Exchange
from simulator.strategy import ArbitrageAgent

class LatencyArbitrageSimulator:
    def __init__(self, config):
        self.env = simpy.Environment()
        self.config = config
        self.exchanges = []
        self.agent = None
        self.results = []

    def setup(self):
        for exchange_cfg in self.config["exchanges"]:
            ex = Exchange(
                env=self.env,
                name=exchange_cfg["name"],
                base_price=exchange_cfg.get("base_price", 100.0),
                jitter=exchange_cfg.get("jitter", 0.5),
                update_interval=exchange_cfg.get("update_interval", 0.2)
            )
            self.exchanges.append(ex)

        latency_matrix = self.config.get("latency_matrix", {})
        self.agent = ArbitrageAgent(
            env=self.env,
            name="FastGabiBot",
            exchanges=self.exchanges,
            latency_matrix=latency_matrix,
            config=self.config["agent"],
            results=self.results,
        )

    def run(self, until=10):
        self.setup()
        self.env.run(until=until)
        return self.results