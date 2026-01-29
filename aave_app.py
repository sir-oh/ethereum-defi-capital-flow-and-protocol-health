import time
import requests
import pandas as pd
import streamlit as st

# ---------------------------
# Page config
# ---------------------------
st.set_page_config(
    page_title="Aave v3 – Capital Flow Analysis",
    layout="wide"
)

st.title("🟣 Aave v3 Capital Flow & Usage Quality Dashboard")

st.markdown("""
This dashboard analyzes **capital behavior on Aave v3** using TVL data.

We focus on:
- Capital inflows and outflows
- Net flow momentum
- Capital stability over time

This helps separate **real usage** from **short-term speculative capital**.
""")

# ---------------------------
# Data Fetching
# ---------------------------
@st.cache_data(ttl=3600)
def fetch_aave():
    url = "https://api.llama.fi/protocol/aave"

    for attempt in range(3):
        try:
            r = requests.get(url, timeout=10)
            r.raise_for_status()
            data = r.json()

            df = pd.DataFrame(data["tvl"])
            df["date"] = pd.to_datetime(df["date"], unit="s")
            df = df.sort_values("date")

            df["net_flow"] = df["totalLiquidityUSD"].diff()
            df["rolling_volatility"] = df["net_flow"].rolling(14).std()

            return df

        except requests.exceptions.RequestException:
            if attempt < 2:
                time.sleep(2)
            else:
                return None


# ---------------------------
# Load data
# ---------------------------
df = fetch_aave()

if df is None or df.empty:
    st.error("⚠️ Aave data is temporarily unavailable. Please refresh later.")
    st.stop()

# ---------------------------
# KPIs
# ---------------------------
col1, col2 = st.columns(2)

col1.metric(
    "Current TVL (USD)",
    f"${df.iloc[-1]['totalLiquidityUSD']:,.0f}"
)

col2.metric(
    "Average Daily Net Flow",
    f"${df['net_flow'].mean():,.0f}"
)

# ---------------------------
# Charts
# ---------------------------
st.subheader("📈 Total Value Locked (TVL)")
st.line_chart(
    df.set_index("date")["totalLiquidityUSD"]
)

st.caption("Shows how total supplied capital on Aave has evolved.")

st.subheader("🔁 Net Capital Flow")
st.bar_chart(
    df.set_index("date")["net_flow"]
)

st.caption("Positive values = net deposits, negative = withdrawals.")

st.subheader("🧠 Capital Stability (14D Volatility)")
st.line_chart(
    df.set_index("date")["rolling_volatility"]
)

st.caption("Lower volatility suggests stable, long-term usage.")

# ---------------------------
# Final Insight
# ---------------------------
st.markdown("""
### 🔍 Key Takeaway

Aave’s strength is not just **how much capital it has**,  
but **how that capital behaves over time**.

Sustained inflows and low volatility signal healthy protocol usage.
""")
