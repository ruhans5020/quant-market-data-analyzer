"""Simple vectorized long-only backtester."""
from dataclasses import dataclass
import pandas as pd
from .metrics import performance_summary

@dataclass
class BacktestResult:
    equity: pd.Series
    returns: pd.Series
    positions: pd.Series
    trades: pd.Series
    metrics: dict

def run_backtest(close: pd.Series, signal: pd.Series, initial_capital=100000.0, transaction_cost=0.001, slippage=0.0005):
    pos=signal.fillna(0).astype(float).shift(1).fillna(0)
    asset_ret=close.pct_change().fillna(0)
    turnover=pos.diff().abs().fillna(pos.abs())
    costs=turnover*(transaction_cost+slippage)
    strat_ret=pos*asset_ret-costs
    equity=initial_capital*(1+strat_ret).cumprod()
    return BacktestResult(equity,strat_ret,pos,turnover,performance_summary(strat_ret))
