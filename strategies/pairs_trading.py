from quantlab.indicators import zscore
def pairs_signal(spread,window=60,threshold=2):
 z=zscore(spread,window); return z.lt(-threshold).astype(int)-z.gt(threshold).astype(int)
