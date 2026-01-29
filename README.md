**Project 4 — DeFi Capital Flow & Protocol Health (Ethereum)**
**Overview**

This project analyzes capital flows and liquidity stability across major Ethereum DeFi protocols: Aave v3, Uniswap, and Curve.

Instead of focusing only on TVL size, the analysis evaluates how capital behaves over time.

**Problem Statement**

Protocol health depends not just on how much capital is deposited, but on whether that capital is stable, sticky, and resilient to market conditions.

**Data**

1. Protocol-level TVL data

2. Historical liquidity and usage trends

3. Time-series capital flow metrics

**Methodology**

1. Retrieved protocol data via DeFiLlama API

2. Computed daily net inflows and outflows

3. Measured rolling volatility to assess capital stability

4. Built protocol-specific dashboards using Streamlit

**Key Insights**

1. Lending protocols show different capital dynamics than DEXs

2. High volatility often signals speculative or incentive-driven capital

3. Stable net flows indicate long-term user confidence

**Tools**

Python · Streamlit · DeFiLlama API · Time-series analysis
