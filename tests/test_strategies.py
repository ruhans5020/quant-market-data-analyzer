import pandas as pd
from quantlab.strategies import moving_average_crossover

def test_ma_signal():
    s=pd.Series(range(1,101),dtype=float); x=moving_average_crossover(s,5,20); assert set(x.dropna().unique()) <= {0,1}
