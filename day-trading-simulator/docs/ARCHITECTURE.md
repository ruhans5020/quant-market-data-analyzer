# Architecture

TradeForge separates the simulator into data, execution, portfolio, risk, orchestration, and UI layers.

1. Data loads historical/delayed market bars and indicators.
2. Execution estimates bid/ask, slippage, participation, and order triggers.
3. Portfolio maintains cash, positions, average cost, realized P&L, and mark-to-market equity.
4. Risk checks buying power, concentration, and daily loss limits.
5. Simulator coordinates orders, bars, fills, and portfolio updates.
6. UI exposes the simulator through Streamlit.

The simulator never calls a brokerage API. A fixed random seed makes the execution model reproducible for tests.
