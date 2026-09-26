import pandas as pd
from quantlab.indicators import zscore

def pairs_signal(spread: pd.Series, window=60, threshold=2.0):
    z=zscore(spread,window); return pd.Series(0,index=spread.index).where(False,0).mask(z<-threshold,1).mask(z>threshold,-1)
