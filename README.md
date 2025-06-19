# Latency Arbitrage Simulator

Welcome to the Latency Arbitrage Simulator! A playful yet powerful simulation project which Im designing to explore and analyze latency arbitrage strategies in electronic trading environments. Say its a personal lab for understanding how tiny time differences can drive profit in fast-paced financial markets

## Purpose
This project simulates how latency arbitrage works, where traders exploit small delays in market data across exchanges to execute faster trades and lock in profits. Especially relevant in high-frequency trading (HFT), and more broadly in the wild world of crypto where MEV bots, sandwich attacks, and frontrunning shenanigans are part of your daily breakfast (been there, done that 🤡)

As someone who's dabbled in the degenerate jungle of shitcoin trading, I know first-hand the heartbreak of slow fills and slippage that eats your soul. This simulator is my nerdy revenge: a way to model, visualize and outsmart the latency gods (suck it, Jaredfromsubway)

![image](https://github.com/user-attachments/assets/b3698f1c-3ca6-4f23-ae9a-5107f064725f)

We’ll explore:

- How microseconds can separate winners from bagholders
- Simulating synthetic latency across multiple exchanges
- Designing agent-based strategies that react fast (like, really fast)
- Logging and visualizing trade outcomes, decision speed and PnL curves

## Project Roadmap
Here's how the simulation will evolve over time. Each phase introduces additional realism, complexity, and fun:

### Phase 1: Core Infrastructure
- [x] Set up repo with `poetry`, `pyproject.toml`, clean file structure
- [ ] Simulate two exchanges with artificial latency using `SimPy`
- [ ] Create agents that can detect and act on arbitrage opportunities
- [ ] Lose my mind and question my whole existance at 2am
- [ ] Output trades, latencies, and results to dataframes

### Phase 2: Visualization + Analytics
- [ ] Add visualizations with `plotly` & `streamlit`
- [ ] Real-time dashboard showing trade activity, PnL, latency gaps
- [ ] Metrics around win/loss rate, execution speed, and opportunity frequency

### Phase 3: Strategy Experiments
- [ ] Add parameter tuning (latency gaps, strategy thresholds)
- [ ] Compare passive vs. aggressive arbitrage approaches
- [ ] Add exchange simulation variance (jitter, downtime)

### Phase 4: ML Exploration (Pray I reach this phase)
- [ ] Use simple ML models to predict latency windows
- [ ] Adaptive agents that tweak strategy based on past performance

## Tech Stack
- **Python** (>=3.11)
- **SimPy** – discrete event simulation engine
- **Streamlit** – UI for dashboards
- **Plotly / Matplotlib** – charts and visuals
- **Poetry** – dependency and environment manager
- **Pandas / NumPy** – for data manipulation

## Project Structure
```
latency-arbitrage-simulator/
├── src/                   # core simulation code lives here
│   └── main.py            # entry point for simulating latency arbitrage
│
├── notebooks/             # Jupyter notebooks for quick testing & analysis
│
├── tests/                 # pytest-based unit tests
│
├── pyproject.toml         # project metadata, dependencies, config (poetry)
├── poetry.lock            # exact locked versions of all dependencies
├── README.md              # you're looking at it 
└── .gitignore             # keep it clean, keep it lean

```

##  Why This Project?
I created this as part of a tailored application to demonstrate my skills in simulation modeling, trading systems, and creative problem solving. It’s a way to shocase my passion (obsession?) with building it from scratch, asking questions, spiralling occasionally, and designing things that are beautiful and insightful. It’s my version of a digital playground. Somehow I still manage to work out 6 days a week...

##  Want to Collaborate or Hire Me?
I’m Gabriella Mansur — a mechanical engineer turned data engineer turned crypto degen turned god knows what, creative problem solver, and endlessly curious mind. HMU! (by text or mail - im still a millennial and weirdly terrified of unexpected calls) [LinkedIn](https://linkedin.com/in/gabriellamansur)

Disclaimer: No actual shitcoins were harmed in the making of this repo.
