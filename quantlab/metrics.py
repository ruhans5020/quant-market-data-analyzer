"""Performance and risk metrics."""
import numpy as np
import pandas as pd

def total_return(r): return (1+r.fillna(0)).prod()-1

def annualized_return(r, periods=252):
    n=r.dropna().shape[0]
    return (1+total_return(r))**(periods/n)-1 if n else np.nan

def annualized_volatility(r, periods=252): return r.std()*np.sqrt(periods)
def sharpe_ratio(r, risk_free_rate=0.0, periods=252):
    rf=(1+risk_free_rate)**(1/periods)-1
    excess=r.dropna()-rf
    return np.nan if excess.std()==0 else excess.mean()/excess.std()*np.sqrt(periods)
def sortino_ratio(r, risk_free_rate=0.0, periods=252):
    rf=(1+risk_free_rate)**(1/periods)-1; excess=r.dropna()-rf; downside=excess[excess<0].std()
    return np.nan if downside==0 else excess.mean()/downside*np.sqrt(periods)
def max_drawdown(r):
    wealth=(1+r.fillna(0)).cumprod(); return (wealth/wealth.cummax()-1).min()
def calmar_ratio(r):
    dd=abs(max_drawdown(r)); return np.nan if dd==0 else annualized_return(r)/dd
def win_rate(r): return (r.dropna()>0).mean()
def value_at_risk(r, confidence=.95): return -r.dropna().quantile(1-confidence)
def expected_shortfall(r, confidence=.95):
    x=r.dropna(); var=x.quantile(1-confidence); return -x[x<=var].mean()
def performance_summary(r):
    return {"Total Return":total_return(r),"Annualized Return":annualized_return(r),"Volatility":annualized_volatility(r),"Sharpe":sharpe_ratio(r),"Sortino":sortino_ratio(r),"Max Drawdown":max_drawdown(r),"Calmar":calmar_ratio(r),"Win Rate":win_rate(r),"VaR 95%":value_at_risk(r),"Expected Shortfall 95%":expected_shortfall(r)}
