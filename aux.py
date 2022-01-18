import time
import panterbot.driver as pb
from panterbot.data.fetch import get_data

def trading_session(TSDict):

  # Selector
  if (TSDict['strategy'] == 'basic'):
    from panterbot.strategies.basic import seektrade as seektrade 
    from panterbot.strategies.basic import seekexit as seekexit



  # Run
  l_session_running = True
  l_trade_open=False
  outcome_list = []

  if pb.is_realtime(TSDict):
    while l_session_running:
      if not l_trade_open:
        data = get_data()
        l_trade_open, objeto = seektrade(data,TSDict) 
        if not l_trade_open: time.sleep(10)
      if l_trade_open:
        data = get_data()
        l_trade_open, objeto = seekexit(data,TSDict,objeto)
        if not l_trade_open : outcome_list.append(objeto['outcome'])

  if pb.is_backtest(TSDict):
    data = get_data(lookback='1440 min ago GMT')
    for t in range(30,len(data)):
      simul_time = data.index[t]
      if not l_trade_open:
        l_trade_open, objeto = seektrade(data.loc[data.index < simul_time],TSDict)
      if l_trade_open:
        l_trade_open, objeto = seekexit(data.loc[data.index < simul_time],TSDict,objeto)
        if not l_trade_open : outcome_list.append(objeto['outcome'])

  #accumulate trade objets in a list
  #return a list of trade objects
  return outcome_list




