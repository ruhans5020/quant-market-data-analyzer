def drawdown(returns):
 w=(1+returns.fillna(0)).cumprod(); return w/w.cummax()-1
def rolling_volatility(returns,window=20): return returns.rolling(window).std()*252**.5
def rolling_sharpe(returns,window=60): return returns.rolling(window).mean()/returns.rolling(window).std()*252**.5
