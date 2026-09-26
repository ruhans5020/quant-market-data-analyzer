import streamlit as st
import matplotlib.pyplot as plt
from quantlab.data import download_market_data
from quantlab.strategies import moving_average_crossover,momentum_strategy,mean_reversion,bollinger_mean_reversion
from quantlab.backtester import run_backtest
from quantlab.portfolio import buy_and_hold_returns
from quantlab.metrics import performance_summary
from quantlab.risk import drawdown
st.set_page_config(page_title="QuantLab",layout="wide")
st.title("QuantLab")
st.caption("Quantitative Finance Research & Backtesting Platform")
ticker=st.sidebar.text_input("Ticker","SPY"); start=st.sidebar.date_input("Start",value=__import__('datetime').date(2018,1,1)); end=st.sidebar.date_input("End",value=__import__('datetime').date.today())
strategy=st.sidebar.selectbox("Strategy",["Moving Average","Momentum","Mean Reversion","Bollinger Mean Reversion"]); cost=st.sidebar.number_input("Transaction cost",0.0,0.02,0.001,0.0005); capital=st.sidebar.number_input("Initial capital",1000.0,10000000.0,100000.0)
try:
 df=download_market_data(ticker,str(start),str(end)); close=df.Close
 if strategy=="Moving Average": signal=moving_average_crossover(close,20,50)
 elif strategy=="Momentum": signal=momentum_strategy(close,60)
 elif strategy=="Mean Reversion": signal=mean_reversion(close,20,1.5)
 else: signal=bollinger_mean_reversion(close,20,2)
 result=run_backtest(close,signal,capital,cost); bench=capital*(1+buy_and_hold_returns(close)).cumprod()
 st.subheader("Equity Curve"); st.line_chart(__import__('pandas').DataFrame({"Strategy":result.equity,"Buy & Hold":bench}))
 cols=st.columns(6); m=result.metrics
 for c,(k,v) in zip(cols,list(m.items())[:6]): c.metric(k,f"{v:.2%}" if "Return" in k or "Drawdown" in k or "Volatility" in k or "Rate" in k else f"{v:.2f}")
 st.subheader("Drawdown"); st.line_chart(drawdown(result.returns))
 with st.expander("Research notes"):
  st.write("Signals are shifted one period before returns are applied to reduce look-ahead bias. Transaction costs are modeled explicitly. Historical backtests are not predictions of future performance.")
except Exception as e: st.error(f"Unable to load or analyze data: {e}")
