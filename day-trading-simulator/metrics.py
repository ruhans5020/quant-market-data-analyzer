import numpy as np

def performance_metrics(equity):
    returns = equity.pct_change().dropna()
    if returns.empty:
        return {}
    peak = equity.cummax()
    drawdown = equity / peak - 1
    sharpe = np.sqrt(252 * 78) * returns.mean() / returns.std() if returns.std() else 0.0
    wins = returns[returns > 0]
    losses = returns[returns < 0]
    profit_factor = wins.sum() / abs(losses.sum()) if not losses.empty else float('inf')
    return {'total_return': float(equity.iloc[-1] / equity.iloc[0] - 1), 'max_drawdown': float(drawdown.min()), 'sharpe': float(sharpe), 'win_rate': float((returns > 0).mean()), 'profit_factor': float(profit_factor)}
