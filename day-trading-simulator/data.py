import pandas as pd
import yfinance as yf

def load_market_data(symbol: str, period='5d', interval='5m') -> pd.DataFrame:
    data = yf.download(symbol, period=period, interval=interval, auto_adjust=False, progress=False)
    if data.empty:
        raise ValueError(f'No market data returned for {symbol}.')
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)
    data = data.rename(columns=str.lower)
    required = ['open', 'high', 'low', 'close', 'volume']
    missing = [c for c in required if c not in data.columns]
    if missing:
        raise ValueError(f'Missing market fields: {missing}')
    return data[required].dropna()

def add_indicators(df):
    out = df.copy()
    out['sma20'] = out['close'].rolling(20).mean()
    out['ema9'] = out['close'].ewm(span=9, adjust=False).mean()
    typical = (out['high'] + out['low'] + out['close']) / 3
    out['vwap'] = (typical * out['volume']).cumsum() / out['volume'].cumsum()
    delta = out['close'].diff()
    gain = delta.clip(lower=0).rolling(14).mean()
    loss = (-delta.clip(upper=0)).rolling(14).mean()
    rs = gain / loss.replace(0, pd.NA)
    out['rsi14'] = 100 - (100 / (1 + rs))
    return out
