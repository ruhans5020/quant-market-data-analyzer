import pandas as pd
from quantlab.backtester import run_backtest
def test_signal_is_lagged():
 close=pd.Series([100,101,102,103]); signal=pd.Series([0,1,1,1]); result=run_backtest(close,signal,transaction_cost=0,slippage=0); assert result.positions.iloc[1]==0; assert result.positions.iloc[2]==1
