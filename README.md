Project 4 — DeFi Capital Flow & Protocol Health (Ethereum)
Overview

This project analyzes capital flows and liquidity stability across major Ethereum DeFi protocols: Aave v3, Uniswap, and Curve.

Instead of focusing only on TVL size, the analysis evaluates how capital behaves over time.

Problem Statement

Protocol health depends not just on how much capital is deposited, but on whether that capital is stable, sticky, and resilient to market conditions.

Data

Protocol-level TVL data

Historical liquidity and usage trends

Time-series capital flow metrics

Methodology

Retrieved protocol data via DeFiLlama API

Computed daily net inflows and outflows

Measured rolling volatility to assess capital stability

Built protocol-specific dashboards using Streamlit

Key Insights

Lending protocols show different capital dynamics than DEXs

High volatility often signals speculative or incentive-driven capital

Stable net flows indicate long-term user confidence

Tools

Python · Streamlit · DeFiLlama API · Time-series analysis