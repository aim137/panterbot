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
  t_skip = None
  outcome_list = []

  if pb.is_realtime(TSDict):
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

  if pb.is_backtest(TSDict):
    data = get_data(lookback='111440 min ago GMT')
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

