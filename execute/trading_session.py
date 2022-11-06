import time
import panterbot.driver as pb
from panterbot.data.fetch import get_data
from panterbot.auxlib.functions import is_realtime,is_backtest
import pandas as pd


class TradingSession():

  def __init__(self,
               data: pd.DataFrame,
               strategy):
    self.data = data
    self.data.drop(self.data.head(1).index,inplace=True)
    self.strategy = strategy

  def run(self,TSdict):
    l_session_running = True
    l_trade_open = False
    strat = self.strategy(TSdict)
    while l_session_running:
      time.sleep(300)
      data = get_data(TSdict)
      self.data = self.data.append(data)
      l_buy,l_sell = strat.evaluate(self.data,l_trade_open) 
      print(str(self.data.index[-1])+'  '+str(l_buy)+'  '+str(l_sell))
      if l_buy:
        l_trade_open = True
        print('Bought at price: '+str(self.data.Close[-1]))
      if l_sell:
        l_trade_open = False
        print('Sold at price: '+str(self.data.Close[-1]))

























def trading_session(TSDict):
  """ OLD FUNCTION TO BE DEPRECATED """

  # Selector
  if (TSDict['STRATEGY']['name'] == 'basic'):
    from panterbot.strategies.basic import seektrade as seektrade 
    from panterbot.strategies.basic import seekexit as seekexit



  # Run
  l_session_running = True
  l_trade_open=False
  t_skip = None
  outcome_list = []
  l_mode_RT = is_realtime(TSDict)


  if is_realtime(TSDict):
    while l_session_running:
      if not l_trade_open:
        data = get_data()
        l_trade_open, objeto = seektrade(data,TSDict) 
        if not l_trade_open: time.sleep(60)
        print('Profit: '+str(
                   outcome_list.count('profit')*.25
                  -outcome_list.count('loss')*.15)+'%')
      if l_trade_open:
        data = get_data()
        l_trade_open, objeto = seekexit(data,TSDict,objeto)
        if not l_trade_open : outcome_list.append(objeto['outcome'])

  if is_backtest(TSDict):
    data = get_data(lookback='11117 min ago GMT')
    for t in range(30,len(data)):
      simul_time = data.index[t]
      if not l_trade_open:
#       t_skip, l_skip = skip_turn(t,outcome_list,t_skip)
#       if l_skip: continue
        l_trade_open, objeto = seektrade(data.loc[data.index < simul_time],TSDict)
      if l_trade_open:
        l_trade_open, objeto = seekexit(data.loc[data.index < simul_time],TSDict,objeto)
        if not l_trade_open : outcome_list.append(objeto['outcome'])

  #accumulate trade objets in a list
  #return a list of trade objects
  return outcome_list


def skip_turn(t,list,t_skip=None):
  if (list[-4:-1].count('loss') <= 3):
    return None, False
  else:
    if t_skip is None: return t, True
    if t_skip is not None:
      if t_skip + 2 >= t: 
        return t_skip, True
      else:
        return None, False

