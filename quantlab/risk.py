"""Risk analysis helpers."""
import pandas as pd
from .metrics import max_drawdown, value_at_risk, expected_shortfall

def drawdown(returns):
    wealth=(1+returns.fillna(0)).cumprod(); return wealth/wealth.cummax()-1
def rolling_volatility(returns, window=20): return returns.rolling(window).std()*252**0.5
def rolling_sharpe(returns, window=60):
    return returns.rolling(window).mean()/returns.rolling(window).std()*252**0.5
