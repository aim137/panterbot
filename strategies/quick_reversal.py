from backtesting import Strategy
from backtesting.lib import crossover
import pandas as pd
import ta


class Quick_Reversal(Strategy):
  """ Strategy Class which inherits from the class Strategy
      as defined in the backtesting library. """
  # Class variables:
  stop_loss = 0.97
  take_profit = 1.045
  delta_t_long  = 10
  delta_t_short = 5
  short_thrs = 0.015
  long_thrs = 0.

  def init(self):
    self.new_df = pd.DataFrame(data=self.data.Close,index=self.data.index)
    desc_l = str(self.delta_t_long)+'m_ret'
    self.new_df[desc_l] = self.new_df.Close / self.new_df.Close.shift(self.delta_t_long) - 1
    desc_s = str(self.delta_t_short)+'m_ret'
    self.new_df[desc_s] = self.new_df.Close / self.new_df.Close.shift(self.delta_t_short) - 1
    self.new_df['signal'] = (self.new_df[desc_l] > 0) & (self.new_df[desc_s] < -0.015)

  def next(self):
  
    if (self.data.index.shape[0] < 1+self.delta_t_long): return
    price = self.data.Close
    longreturn  = self.data.Close[-1]/self.data.Close[-1-self.delta_t_long]  - 1
    shortreturn = self.data.Close[-1]/self.data.Close[-1-self.delta_t_short] - 1
    if (longreturn > self.long_thrs) and (shortreturn < -1*abs(self.short_thrs)):
      print('compre')
      sl = price * self.stop_loss
      tp = price * self.take_profit
      self.buy(sl=sl,tp=tp)
