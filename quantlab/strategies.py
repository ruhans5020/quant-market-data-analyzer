from .indicators import sma,momentum,zscore,bollinger_bands
def moving_average_crossover(close,short=20,long=50): return (sma(close,short)>sma(close,long)).astype(int)
def momentum_strategy(close,lookback=60): return (momentum(close,lookback)>0).astype(int)
def mean_reversion(close,window=20,threshold=1.5): return (zscore(close,window)<-threshold).astype(int)
def bollinger_mean_reversion(close,window=20,num_std=2): return (close<bollinger_bands(close,window,num_std)[2]).astype(int)
