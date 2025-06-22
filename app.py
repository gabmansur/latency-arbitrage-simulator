import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

import streamlit as st
import pandas as pd
import random
import plotly.express as px

# === PLACEHOLDER: Import your actual simulator classes here ===
from src.simulator.core import LatencyArbitrageSimulator

# ------------------- 1. Header & Dummy Explanation -------------------

st.set_page_config(page_title="Latency Arbitrage Simulator", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
    <link href="https://fonts.googleapis.com/css?family=Poppins:700,900&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

# Gradient title
st.markdown(
    """
    <h1 style='
        text-align: center;
        font-size: 3.5rem;
        font-family: "Poppins", "Segoe UI", Arial, sans-serif;
        background: linear-gradient(90deg, #e876f8 10%, #5de0fc 90%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900;
        margin-bottom: 0.3em;
    '>
        Latency Arbitrage Simulator 🦄⚡
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div style='text-align: center;'>
        <img src='https://media.tenor.com/rI_0O_9AJ5sAAAAj/nyan-cat-poptart-cat.gif' width='320'>
    </div>
    """,
    unsafe_allow_html=True
)

st.caption("by Gabi | Code Witch & Basement Goblin")
st.markdown(
    '[View the GitHub Repo](https://github.com/gabmansur/latency-arbitrage-simulator) &nbsp; | &nbsp; ⭐ Star it to power up the goblin energy!'
)

with st.expander("🍼 Explain Like I'm 5 (The Real Dummy Guide)"):
    st.markdown("""
    > **What is this?**
    >
    > Imagine you have two lemonade stands, but each one tells you the price of lemonade at a slightly different time.  
    > If you notice the price is lower at Stand A and higher at Stand B, you could buy lemonade at A and quickly sell it at B to make some money.  
    >
    > But… if you’re too slow, the prices might change before you can finish your trade, and you miss out.  
    > The *faster* you are, the more likely you win!
    >
    > This simulator lets you be the sneaky lemonade goblin, setting how fast you are, how greedy you want to be, and how quickly you spot deals. Then you watch to see if you score a win, or get beat by the lag monsters!
    >
    > 🦄 **Try it! Play with the sliders. Hit ‘Run Simulation’. See if you get rich or rekt!**
    """)


# ---  Connected "How to Play" + Dummy Guide + Run Button ---
with st.container():
    col_left, col_center, col_right = st.columns([2,2,2])
    with col_center:
        st.markdown("""
        <div style='
            background:rgba(200,160,255,0.13);
            border:1.5px solid #bb80f8;
            border-radius:16px;
            padding:2.2em 2.2em 1.3em 2.2em;
            margin-top:1.2em;
            margin-bottom:1.2em;
            text-align:center;
            '>
            <h3 style="margin-bottom:0.7em;"><b>How to Play:</b></h3>
            <div style="text-align:left; max-width:420px; margin:auto;">
                <b>Step 1:</b> Set parameters in the <span style="color:#bb80f8;">sidebar</span>.<br>
                <b>Step 2:</b> Click <b style="color:#e370fd;">Run Simulation</b> below.<br>
                <b>Step 3:</b> Laugh, cry, and try new settings for even juicier arbs.<br>
                <span style="font-size:0.93em; color:#999;">(Hint: Hover sliders for tips!)</span>
            </div>
            <br>
        """, unsafe_allow_html=True)

        # Place the big run button here!
        run = st.button("Run Simulation!", key="centered_run_btn", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

# ------------------- 2. Sidebar Controls (with tooltips) -------------------

with st.sidebar:
    st.header("Simulation Controls")
    exchange_1_name = st.text_input("Exchange 1 Name", value="Binance", help="What should we call the first exchange?")
    exchange_2_name = st.text_input("Exchange 2 Name", value="Coinbase", help="And the second one?")
    binance_latency = st.slider(
        f"{exchange_1_name} Latency (ms)", 0, 500, 125,
        help=f"Milliseconds for trades/data to reach {exchange_1_name}. Lower = faster bot!"
    )
    coinbase_latency = st.slider(
        f"{exchange_2_name} Latency (ms)", 0, 500, 150,
        help=f"How slow is {exchange_2_name}? Sometimes lag is your friend!"
    )
    win_rate = st.slider(
    "Win Rate (%)", 50, 100, 90,
    help="Simulate what percentage of trades your bot actually wins (rest are fails)."
    )
    threshold = st.slider(
        "Arbitrage Threshold ($)", 0.01, 2.0, 0.5,
        help="Min price gap for your bot to act. Low = aggressive, high = cautious."
    )
    reaction_time = st.slider(
        "Agent Reaction Time (ms)", 10, 1000, 350,
        help="How quickly your bot reacts when it spots a trade. 1000ms = boomer, 10ms = turbo giga-chad."
    )
    sim_time = st.slider(
        "Simulation Time (s)", 1, 60, 10,
        help="How many seconds should the simulation run for?"
    )

    st.markdown("—")
    if st.button("🔄 Reset Parameters"):
        try:
            st.rerun()
        except AttributeError:
            st.experimental_rerun()

# -------------------  3. Run Simulation ------------------- 
def run_simulation(
    binance_latency, coinbase_latency, threshold, reaction_time, sim_time
):
    config = {
        "exchanges": [
            {"name": exchange_1_name, "latency_ms": binance_latency},
            {"name": exchange_2_name, "latency_ms": coinbase_latency},
        ],
        "agent": {
            "price_diff_threshold": threshold,
            "reaction_time": reaction_time / 1000.0,  # ms to seconds
            "win_rate": win_rate / 100,  # as a probability
        }
    }
    sim = LatencyArbitrageSimulator(config)
    results = sim.run(until=sim_time)
    return results

results = None
if run:
    with st.spinner("Simulating... May the arbitrage gods be with you!"):
        results = run_simulation(
            binance_latency, coinbase_latency, threshold, reaction_time, sim_time
        )
        df = pd.DataFrame(results)

        st.success("Simulation Complete!")

# -------------------  4. Analytics, Plots, and Explanations ------------------- 
if run and results and len(results) > 0:
    st.subheader("📊 Simulation Results")
    df = pd.DataFrame(results)
    total_trades = len(df)
    num_wins = (df['success'] == True).sum()
    win_rate = 100 * num_wins / total_trades if total_trades > 0 else 0
    total_pnl = df['spread'].sum()
    avg_latency = df['latency'].mean()
    biggest_win = df['spread'].max()
    biggest_loss = df['spread'].min()

    colA, colB, colC, colD, colE = st.columns(5)
    colA.metric("Total Trades", total_trades)
    colB.metric("Total PnL ($)", f"{total_pnl:.4f}")
    colC.metric("Avg Latency (s)", f"{avg_latency:.3f}")
    colD.metric("Biggest Win ($)", f"{biggest_win:.3f}")
    colE.metric("Win Rate (%)", f"{win_rate:.1f}")

    # Side by side plots
    c1, c2 = st.columns(2)
    with c1:
        st.plotly_chart(
            px.line(df, y="spread", title="PnL per Trade", labels={"spread": "Profit ($)"}),
            use_container_width=True
        )
    with c2:
        st.plotly_chart(
            px.line(df, y=df['spread'].cumsum(), title="Cumulative PnL Over Time", labels={"y": "Total Profit ($)"}),
            use_container_width=True
        )

    # Table
    st.dataframe(df.style.background_gradient(axis=0, cmap="RdYlGn"), height=400)

    # Insights/explanations section
    with st.expander("📖 What do these numbers mean?"):
        st.markdown("""
        - **Total Trades**: How many times your bot found an opportunity.
        - **PnL**: Profit and Loss (the goal is to print money, not burn it).
        - **Avg Latency**: How slow/fast your bot is.
        - **Biggest Win/Loss**: Your best and worst moments.
        - **Win Rate**: % of trades that were positive.
        - If PnL is red, maybe try tuning latency or reaction time!
        """)

    # Download
    st.download_button(
        "⬇️ Download Results as CSV",
        df.to_csv(index=False).encode(),
        file_name="arbitrage_results.csv"
    )


# Meme Commentary
    # comments = [
    #     "That’s how you snipe the market! 🥷",
    #     "Not bad for a first run. Try raising the threshold next time.",
    #     "Ouch, missed a juicy one! Timing is everything.",
    #     "Goblin's tip: Sometimes the slowest bot wins in a choppy market!",
    #     "If you’re not sweating, you’re not arbing hard enough.",
    #     "The real latency was the friends we made along the way."
    # ]
    # st.info(random.choice(comments))
    # if total_pnl > 0:
    #     st.image("https://media.giphy.com/media/26u4nJPf0JtQPdStq/giphy.gif", caption="WINNING!! 🚀")
    # else:
    #     st.image("https://images3.memedroid.com/images/UPLOADED922/66b0d7a0c83f4.webp", caption="REKT, try again 💀")

    # Missed opportunities placeholder (if you track them in the future)
    # st.warning(f"Missed Opportunities: {missed_ops}")


# else:
    # st.info("Set your simulation parameters in the sidebar and hit 'Run Simulation' to start! (Or break things, it's all good.)")

# Footer
st.markdown("---")
st.caption("Built with ❤️, memes, and coffee by Gabi • [GitHub](https://github.com/gabmansur) • [LinkedIn](https://linkedin.com/in/gabriellamansur) ")
st.image("https://images3.memedroid.com/images/UPLOADED922/66b0d7a0c83f4.webp", width=400)