import numpy as np

def stickiness_score(df):
    flows = df["net_flow"].dropna()
    if flows.std() == 0:
        return 0
    return flows.mean() / flows.std()
