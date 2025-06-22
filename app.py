import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

import streamlit as st
import pandas as pd
from src.simulator.core import LatencyArbitrageSimulator

st.markdown(
    """
    <h1 style='color:#e47dff;'>Latency Arbitrage Simulator 🦄⚡</h1>
    <h4 style='color:#bbdefb;'>Gabi's playground for trading speed and market chaos.</h4>
    """, unsafe_allow_html=True
)
st.image("https://media.tenor.com/rI_0O_9AJ5sAAAAj/nyan-cat-poptart-cat.gif", width=280, caption="High frequency trader IRL")

st.title("Latency Arbitrage Simulator Dashboard")

st.sidebar.header("Simulation Controls")
latency1 = st.sidebar.slider("Binance Latency (ms)", 0, 500, 50, step=5, help="How laggy is Binance for you today? Slower = more heartbreak when you're too slow.")
latency2 = st.sidebar.slider("Coinbase Latency (ms)", 0, 500, 50, step=5)
threshold = st.sidebar.slider("Arb Threshold ($)", 0.01, 2.0, 0.2, step=0.01)
reaction_time = st.sidebar.slider("Agent Reaction Time (ms)", 10, 1000, 100, step=10)
sim_time = st.sidebar.slider("Simulation Time (s)", 1, 30, 10, step=1)

if st.sidebar.button("Run Simulation"):
    config = {
        "exchanges": [
            {"name": "Binance", "latency_ms": latency1},
            {"name": "Coinbase", "latency_ms": latency2},
        ],
        "agent": {
            "price_diff_threshold": threshold,
            "reaction_time": reaction_time / 1000.0,
        },
    }
    simulator = LatencyArbitrageSimulator(config)
    results = simulator.run(until=sim_time)
    df = pd.DataFrame(results)

    st.success("Simulation Complete!")
    st.write(f"Total Trades: {len(df)}")
    st.line_chart(df["spread"])
    st.line_chart(df["pnl"].cumsum() if "pnl" in df else df["spread"].cumsum())
    st.dataframe(df)

    st.caption("Powered by degenerate Gabi-code and simulated crypto adrenaline")
else:
    st.info("Tune your parameters in the sidebar and click 'Run Simulation'!")

