"""Historical market-data utilities."""
from __future__ import annotations
import pandas as pd
import yfinance as yf

REQUIRED_COLUMNS = ["Open", "High", "Low", "Close", "Volume"]

def download_market_data(ticker: str, start: str, end: str, interval: str = "1d") -> pd.DataFrame:
    if not ticker.strip(): raise ValueError("Ticker cannot be empty")
    df = yf.download(ticker, start=start, end=end, interval=interval, auto_adjust=True, progress=False)
    if df.empty: raise ValueError(f"No market data returned for {ticker}")
    if isinstance(df.columns, pd.MultiIndex): df.columns = df.columns.get_level_values(0)
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing: raise ValueError(f"Missing columns: {missing}")
    return clean_market_data(df)

def clean_market_data(df: pd.DataFrame) -> pd.DataFrame:
    out=df.copy().sort_index()
    out=out[~out.index.duplicated(keep="first")]
    out=out.dropna(subset=["Close"])
    out["Return"]=out["Close"].pct_change()
    out["LogReturn"]=__import__("numpy").log(out["Close"]).diff()
    return out
