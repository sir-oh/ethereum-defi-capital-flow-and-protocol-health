import streamlit as st
from utils.fetch import fetch_uniswap
import plotly.express as px

st.set_page_config(
    page_title="Uniswap Capital Flow Analysis",
    layout="wide"
)

st.title("🦄 Uniswap Capital Flow & Liquidity Stickiness")

st.markdown("""
This dashboard analyzes how capital enters and exits Uniswap over time.
By examining **daily changes in TVL**, we can distinguish stable liquidity
from speculative or short-term capital.
""")

df = fetch_uniswap()

fig = px.line(
    df,
    x="date",
    y="net_flow",
    title="Daily Net Capital Flow (USD)"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("""
### What this chart answers

**Question:**  
Is liquidity entering Uniswap consistently or rotating in and out?

**Method:**  
Daily net flow is calculated as the change in Total Value Locked (TVL).
Positive values indicate net inflows, negative values indicate withdrawals.
""")
