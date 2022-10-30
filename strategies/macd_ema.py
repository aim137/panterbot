from backtesting import Strategy
from backtesting.lib import crossover
import pandas as pd
import ta


class Strat_Macd_Ema(Strategy):
  """ Strategy Class which inherits from the class Strategy
      as defined in the backtesting library. """
  # Class variables:
  stop_loss = 0.97
  take_profit = 1.045

  def init(self):
    close = self.data.Close
    self.macd        = self.I(ta.trend.macd,         pd.Series(close))
    self.macd_signal = self.I(ta.trend.macd_signal,  pd.Series(close))
    self.ema         = self.I(ta.trend.ema_indicator,pd.Series(close),window=100)

  def next(self):
    price = self.data.Close
    if crossover(self.macd, self.macd_signal) and price > self.ema:
      sl = price * self.stop_loss
      tp = price * self.take_profit
      self.buy(sl=sl,tp=tp)
