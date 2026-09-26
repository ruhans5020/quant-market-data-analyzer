from dataclasses import dataclass
from .metrics import performance_summary
@dataclass
class BacktestResult: equity: object; returns: object; positions: object; trades: object; metrics: dict
def run_backtest(close,signal,initial_capital=100000,transaction_cost=.001,slippage=.0005):
 pos=signal.fillna(0).astype(float).shift(1).fillna(0); asset=close.pct_change().fillna(0); turnover=pos.diff().abs().fillna(pos.abs()); ret=pos*asset-turnover*(transaction_cost+slippage); equity=initial_capital*(1+ret).cumprod(); return BacktestResult(equity,ret,pos,turnover,performance_summary(ret))
