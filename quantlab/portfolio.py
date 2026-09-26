def buy_and_hold_returns(close): return close.pct_change().fillna(0)
def equal_weight_returns(price_df): return price_df.pct_change().mean(axis=1).fillna(0)
