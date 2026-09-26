import matplotlib.pyplot as plt
def plot_equity(equity,benchmark=None):
 fig,ax=plt.subplots(figsize=(11,5)); equity.plot(ax=ax,label="Strategy")
 if benchmark is not None: benchmark.plot(ax=ax,label="Benchmark")
 ax.set_title("Equity Curve"); ax.set_ylabel("Portfolio Value"); ax.legend(); fig.tight_layout(); return fig
def plot_drawdown(dd):
 fig,ax=plt.subplots(figsize=(11,4)); dd.plot(ax=ax); ax.set_title("Drawdown"); ax.set_ylabel("Drawdown"); fig.tight_layout(); return fig
