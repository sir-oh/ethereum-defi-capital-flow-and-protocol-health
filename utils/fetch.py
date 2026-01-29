import requests
import pandas as pd

def fetch_uniswap():
    url = "https://api.llama.fi/protocol/uniswap-v3"
    r = requests.get(url)
    r.raise_for_status()
    data = r.json()

    df = pd.DataFrame(data["tvl"])
    df["date"] = pd.to_datetime(df["date"], unit="s")
    df = df.sort_values("date")
    df["net_flow"] = df["totalLiquidityUSD"].diff()

    return df
