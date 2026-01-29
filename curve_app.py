import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("💧 Curve Liquidity Stability Analysis")

@st.cache_data(ttl=3600)
def fetch_curve():
    url = "https://api.llama.fi/protocol/curve-dex"
    r = requests.get(url)
    r.raise_for_status()
    data = r.json()

    df = pd.DataFrame(data["tvl"])
    df["date"] = pd.to_datetime(df["date"], unit="s")
    df = df.sort_values("date")

    # for the last 18 months only
    df = df[df["date"] >= pd.Timestamp.today() - pd.Timedelta(days=540)]

    df["net_flow"] = df["totalLiquidityUSD"].diff()
    df["rolling_vaolatility"] = df["net_flow"].rolling(14).std()

    return df

df = fetch_curve()

fig = px.line(
    df,
    x="date",
    y="net_flow",
    title="Curve — Daily Net Liquidity Flow"
)

st.plotly_chart(fig, use_container_width=True)

volatility = df["net_flow"].std()

st.metric("Liquidity Volatility", round(volatility, 2))

st.markdown("""
### What this shows
- Curve liquidity reflects **defensive capital behavior**
- Large outflows often align with market stress
- Low volatility signals stable yield-seeking capital
""")
