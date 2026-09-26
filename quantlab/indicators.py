"""Indicators implemented with pandas/numpy."""
import numpy as np
import pandas as pd

def sma(s, window): return s.rolling(window).mean()
def ema(s, window): return s.ewm(span=window, adjust=False).mean()
def rolling_volatility(returns, window=20): return returns.rolling(window).std()*np.sqrt(252)
def momentum(s, window=20): return s.pct_change(window)
def roc(s, window=20): return s.pct_change(window)*100

def rsi(s, window=14):
    d=s.diff(); gain=d.clip(lower=0).rolling(window).mean(); loss=(-d.clip(upper=0)).rolling(window).mean()
    rs=gain/loss.replace(0,np.nan); return 100-(100/(1+rs))

def bollinger_bands(s, window=20, num_std=2):
    mid=s.rolling(window).mean(); std=s.rolling(window).std()
    return mid, mid+num_std*std, mid-num_std*std

def zscore(s, window=20):
    m=s.rolling(window).mean(); sd=s.rolling(window).std(); return (s-m)/sd.replace(0,np.nan)
