import numpy as np
def sma(s,w): return s.rolling(w).mean()
def ema(s,w): return s.ewm(span=w,adjust=False).mean()
def rolling_volatility(r,w=20): return r.rolling(w).std()*np.sqrt(252)
def momentum(s,w=20): return s.pct_change(w)
def rsi(s,w=14):
 d=s.diff(); gain=d.clip(lower=0).rolling(w).mean(); loss=(-d.clip(upper=0)).rolling(w).mean(); rs=gain/loss.replace(0,np.nan); return 100-100/(1+rs)
def bollinger_bands(s,w=20,k=2):
 m=s.rolling(w).mean(); sd=s.rolling(w).std(); return m,m+k*sd,m-k*sd
def zscore(s,w=20):
 m=s.rolling(w).mean(); sd=s.rolling(w).std(); return (s-m)/sd.replace(0,np.nan)
