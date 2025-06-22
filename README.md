# Latency Arbitrage Simulator 🦄⚡

Welcome to the Latency Arbitrage Simulator!  
A playful, slightly unhinged simulation lab for exploring and visualizing **latency arbitrage** in electronic trading. Here, you get to tinker with bot speed, market delays, reaction time, and win rate — and try to outsmart the market before the market eats you alive.

[Try the live dashboard!)](https://latency-arbitrage-simulator.streamlit.app/)  
*Or clone and run locally for max goblin power.*

---

## What is this? (Explain Like I'm 5)

Imagine you have two lemonade stands (exchanges). They both sell lemonade, but sometimes they change prices at different times.  
If you spot that Stand A is selling lemonade cheaper than Stand B, you could buy from A and *immediately* sell to B for a profit...  
**Unless you're too slow, and prices change before you finish!**  
Your job: tune your bot, hit simulate, and see if you’re a market wizard or just lemonade dust.

---

## How to Use

**1. Set your simulation parameters in the sidebar:**
- Exchange names and individual latency (ms)
- Minimum price difference (arb threshold)
- Bot’s reaction speed (ms)
- Win rate (simulate market failures)
- Total simulation run time (seconds)

**2. Smash that "Run Simulation" button.**  
**3. Watch the charts and stats update live:**
- See your trades, win/loss, average latency, and cumulative profit.
- Download the results as CSV.
- Read meme-level market “wisdom” in real-time.
- Laugh, cry, try again.

---

## Project Features

- **Realistic SimPy-based discrete event simulation** (no blockchains were harmed).
- **Agent-based bot logic** with customizable aggressiveness, latency, and reaction time.
- **Win Rate**: Not every trade is a winner! Simulate missed trades and fails.
- **Interactive Streamlit dashboard**: 
  - Two side-by-side charts (PnL per trade, cumulative PnL)
  - Results table with rainbow coloring
  - Metrics: win rate, biggest win/loss, latency, total PnL, more
  - Download/share buttons
  - Degen vibes, meme images, and random goblin commentary
- **Code is readable and hackable** — build your own strategies, add more exchanges, go nuts.

---

## Project Structure

```text
latency-arbitrage-simulator/
├── app.py              # Streamlit dashboard (main entrypoint!)
├── src/                # core simulator logic
│   └── simulator/
│       ├── __init__.py
│       ├── core.py
│       ├── exchange.py
│       ├── strategy.py
│       └── utils.py
├── notebooks/
│   └── exploration.ipynb
├── tests/
│   └── test_core.py
├── poetry.lock
├── pyproject.toml
└── README.md

## Tech Stack

- **Python 3.11+**
- **SimPy** — discrete event simulation engine
- **Streamlit** — interactive dashboard UI
- **Plotly** — fun, interactive charts
- **Pandas** — results wrangling, dataframes, CSV downloads
- **Poetry** — dependency management (because I’m allergic to requirements.txt chaos)
- **Jupyter** (optional) — for exploratory nerding

---

## Roadmap

### Core Simulator
- [x] Simulate two exchanges with customizable latency
- [x] Bot agent with tunable reaction speed and win rate
- [x] Logging, stats, export
- [x] Streamlit dashboard

### Visualization & UX
- [x] Live charts (PnL, cumulative)
- [x] Results table and downloads
- [x] Meme commentary & visual cues
- [x] ELI5/dummy mode instructions

### Experiments/Future
- [ ] Add more exchange types (DEXs, CEXs, unhinged fantasy ones)
- [ ] Multi-agent tournaments
- [ ] Real data feed integration
- [ ] Machine learning strategies (someday...)
- [ ] Visualize missed arb opportunities and order failures

---

## Why This Project?

I built this as a public playground to show off my simulation modeling, trading systems, and creative approach to coding and dashboards (and also to cope with the trauma of missed trades and rekt bags).  
It’s equal parts nerdy flex, learning experiment, and meme-powered demo.

---

## About Me

I'm Gabriella Mansur:  
Mechanical engineer → data engineer → trading goblin → code witch.  
I love turning chaos into structured, explorable, and beautiful things that help people learn and laugh.  

*Disclaimer: No real money, assets, or meme coins are at risk. All pain is simulated. All wins are virtual. All fun is real.*

---

## Meme Gallery

![nyan cat](https://media.tenor.com/rI_0O_9AJ5sAAAAj/nyan-cat-poptart-cat.gif)

---