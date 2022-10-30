from backtesting import Strategy
from backtesting.lib import crossover
import pandas as pd
import ta

def SMA(values, n):
    """
    Return simple moving average of `values`, at
    each step taking into account `n` previous values.
    """
    return pd.Series(values).rolling(n).mean()



class RTSma_Cross():
    
    def __init__(self,TSdict):
        # Precompute the two moving averages
      self.n1 = TSdict['STRATEGY']['tuning']['n1']
      self.n2 = TSdict['STRATEGY']['tuning']['n2']
      self.sl = TSdict['STRATEGY']['tuning']['sl']
    
    def evaluate(self,data,l_trade_open):

      l_buy = False
      l_sell = False
      # calculate sma1 and sma2 using `data`
      _series = SMA(pd.Series(data.Close),self.n1)
      sma1 = _series[-1]
      _series = SMA(pd.Series(data.Close),self.n2)
      sma2 = _series[-1]

      if not l_trade_open and crossover(sma1, sma2):
        l_buy = True

      elif l_trade_open and crossover(sma2, sma1):
        l_sell = True
      
    # elif l_trade_open and self.data.Close[-1] < self.price * self.sl:
    #   l_sell = True
          
      return l_buy,l_sell

