import pandas as pd
from quantlab.metrics import total_return,max_drawdown,sharpe_ratio

def test_total_return(): assert abs(total_return(pd.Series([.1,-.1]))+0.01)<1e-9
def test_drawdown(): assert max_drawdown(pd.Series([.1,-.2]))<0
def test_sharpe_constant_zero(): assert sharpe_ratio(pd.Series([0.,0.,0.])) != sharpe_ratio(pd.Series([0.,0.,0.]))
