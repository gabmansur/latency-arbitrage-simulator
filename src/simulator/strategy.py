import simpy
from simulator.utils import log_event

class ArbitrageAgent:
    def __init__(self, env, name, exchanges, latency_matrix, reaction_time=1, threshold=0.2, results=None):
        self.env = env
        self.name = name
        self.exchanges = exchanges
        self.latency_matrix = latency_matrix
        self.reaction_time = reaction_time
        self.threshold = threshold
        self.results = results if results is not None else []
        self.env.process(self.run())

    def observe_prices(self):
        prices = {}
        for ex in self.exchanges:
            if ex.price is not None:
                prices[ex.name] = ex.price
        return prices

    def detect_opportunity(self, prices):
        if len(prices) < 2:
            return None, None, None
        sorted_exs = sorted(prices.items(), key=lambda x: x[1])
        buy_ex, sell_ex = sorted_exs[0], sorted_exs[-1]
        spread = sell_ex[1] - buy_ex[1]
        if spread >= self.threshold:
            return buy_ex[0], sell_ex[0], spread
        return None, None, None

    def execute_trade(self, buy_ex_name, sell_ex_name, spread):
        latency = self.latency_matrix.get(buy_ex_name, {}).get(sell_ex_name, 0)
        yield self.env.timeout(latency + self.reaction_time)
        log_event(
            self.env,
            f"{self.name} arbitraged {buy_ex_name} -> {sell_ex_name} | Spread: ${spread:.4f}"
        )
        self.results.append({
            "timestamp": self.env.now,
            "buy_from": buy_ex_name,
            "sell_to": sell_ex_name,
            "spread": spread,
            "latency": latency,
            "reaction_time": self.reaction_time,
        })

    def run(self):
        while True:
            prices = self.observe_prices()
            buy_ex, sell_ex, spread = self.detect_opportunity(prices)
            if buy_ex and sell_ex:
                yield self.env.process(self.execute_trade(buy_ex, sell_ex, spread))
            yield self.env.timeout(0.1)  # Check every 100ms