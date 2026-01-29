import plotly.express as px

def net_flow_chart(df, name):
    return px.line(
        df,
        x="date",
        y="net_flow",
        title=f"{name} — Daily Net Capital Flow",
        labels={"net_flow": "USD"}
    )
