# TradeForge — Paper Day-Trading Simulator

TradeForge is an educational paper-trading simulator designed to model brokerage mechanics without sending real orders or using real money.

## Features
- Virtual cash and buying power
- Market, limit, stop, and stop-limit orders
- Bid/ask spread, slippage, commissions, and partial fills
- Long-only positions with average-cost accounting
- Realized and unrealized P&L
- Risk limits and simulated PDT warnings
- Candlestick charts with VWAP, SMA, EMA, RSI, and volume
- Trade blotter, open orders, positions, equity curve, and event log
- Historical replay mode
- CSV exports
- Automated tests

## Run
```bash
pip install -r requirements.txt
streamlit run app.py
```

This project is simulation-only. It does not connect to a brokerage or place real trades. Market data availability and simulated fills are not guaranteed to match an exchange or broker.
