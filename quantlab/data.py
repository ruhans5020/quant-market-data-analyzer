import pandas as pd
import yfinance as yf
REQUIRED_COLUMNS=["Open","High","Low","Close","Volume"]
def clean_market_data(df):
 out=df.copy().sort_index(); out=out[~out.index.duplicated()]; out=out.dropna(subset=["Close"]); out["Return"]=out.Close.pct_change(); out["LogReturn"]=__import__('numpy').log(out.Close).diff(); return out
def download_market_data(ticker,start,end,interval="1d"):
 df=yf.download(ticker,start=start,end=end,interval=interval,auto_adjust=True,progress=False)
 if df.empty: raise ValueError(f"No market data returned for {ticker}")
 if isinstance(df.columns,pd.MultiIndex): df.columns=df.columns.get_level_values(0)
 missing=[c for c in REQUIRED_COLUMNS if c not in df.columns]
 if missing: raise ValueError(f"Missing columns: {missing}")
 return clean_market_data(df)
