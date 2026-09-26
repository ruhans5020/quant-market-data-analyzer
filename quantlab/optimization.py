"""Parameter sensitivity utilities."""
import pandas as pd
from .backtester import run_backtest

def moving_average_grid(close, short_windows, long_windows, metric="Sharpe"):
    from .strategies import moving_average_crossover
    out=pd.DataFrame(index=short_windows,columns=long_windows,dtype=float)
    for s in short_windows:
        for l in long_windows:
            if s>=l: continue
            out.loc[s,l]=run_backtest(close,moving_average_crossover(close,s,l)).metrics.get(metric)
    return out
