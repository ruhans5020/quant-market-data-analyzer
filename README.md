# QuantLab — Quantitative Finance Research & Backtesting Platform

QuantLab is an educational quantitative-finance research platform for testing trading hypotheses, measuring risk, and comparing strategies against a benchmark.

## What it does
- Downloads and cleans historical OHLCV data
- Calculates quantitative indicators
- Backtests momentum, moving-average, mean-reversion, Bollinger Band, and pairs strategies
- Measures return, volatility, Sharpe, Sortino, drawdown, VaR, and Expected Shortfall
- Models transaction costs and slippage
- Performs parameter sensitivity analysis
- Supports chronological out-of-sample testing
- Runs Monte Carlo bootstrap scenarios
- Provides a Streamlit research dashboard

## Quick start

```bash
pip install -r requirements.txt
streamlit run app/dashboard.py
```

## Example research questions
- Does a momentum signal survive realistic transaction costs?
- How sensitive is a moving-average strategy to parameter changes?
- Does a strategy's risk-adjusted performance persist out of sample?
- How different are strategy drawdowns from buy-and-hold?

## Research principles
QuantLab is designed to study uncertainty rather than promise profits. It avoids look-ahead bias in its signal timing, uses chronological train/test evaluation, exposes transaction costs, and reports losing periods rather than hiding them.

Historical backtests are not predictions. Results can be affected by data quality, survivorship bias, overfitting, regime changes, and modeling assumptions. This project is for education and research, not financial advice.

## Project structure

```
app/                 Streamlit dashboard
quantlab/            Core data, strategy, portfolio, risk, and metrics modules
strategies/          Strategy implementations
tests/               Automated tests
notebooks/           Research notebooks
docs/                Methodology and mathematical background
```

## Future research
Factor models, Fama-French factors, GARCH volatility models, options pricing, Kalman filtering, portfolio optimization, and paper-trading experiments are natural extensions.
