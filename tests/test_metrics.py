import pandas as pd
from quantlab.metrics import total_return,max_drawdown
def test_total_return(): assert abs(total_return(pd.Series([.1,-.1]))+0.01)<1e-9
def test_drawdown_is_negative(): assert max_drawdown(pd.Series([.1,-.2]))<0
