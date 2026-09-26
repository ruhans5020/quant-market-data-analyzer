import numpy as np
def total_return(r): return (1+r.fillna(0)).prod()-1
def annualized_return(r,p=252):
 n=r.dropna().shape[0]; return (1+total_return(r))**(p/n)-1 if n else np.nan
def annualized_volatility(r,p=252): return r.std()*np.sqrt(p)
def sharpe_ratio(r,risk_free_rate=0,p=252):
 rf=(1+risk_free_rate)**(1/p)-1; x=r.dropna()-rf; return np.nan if x.std()==0 else x.mean()/x.std()*np.sqrt(p)
def max_drawdown(r):
 w=(1+r.fillna(0)).cumprod(); return (w/w.cummax()-1).min()
def value_at_risk(r,c=.95): return -r.dropna().quantile(1-c)
def expected_shortfall(r,c=.95):
 x=r.dropna(); q=x.quantile(1-c); return -x[x<=q].mean()
def performance_summary(r): return {"Total Return":total_return(r),"Annualized Return":annualized_return(r),"Volatility":annualized_volatility(r),"Sharpe":sharpe_ratio(r),"Max Drawdown":max_drawdown(r),"VaR 95%":value_at_risk(r),"Expected Shortfall 95%":expected_shortfall(r)}
