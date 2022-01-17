#start
import time
from panterbot.aux import run_strategy
from panterbot.data.fetch import get_data

def run(TSDict):

  if (TSDict['MODE'] == 'TRADE'):
    key = input('Vas a usar dinero real? \n')
    if (key != 'paga la panter'): return

  if (TSDict['MODE'] == 'TRADE') or (TSDict['MODE'] == 'SIMULATION'):
    print('entering while loop')
    while True:
      data = get_data()
      run_strategy(data,TSDict)
  else:
    print('entering backtest')
    data = get_data(lookback='1440 min ago GMT')
    l_trade_open = False
    for t in range(30,len(data)):
      if (not l_trade_open):
        l_shouldbuy = run_strategy(data[:t],TSDict)
        print(l_shouldbuy)
        if (l_shouldbuy): l_trade_open = True
      else:
        l_shouldexit = run_strategy(data[:t],TSDict,l_trade_open = True)
        print('should I exit? = '+str(l_shouldexit))
        if (l_shouldexit): l_trade_open = False


def is_backtest(TSDict):
  if (TSDict['MODE'] == 'TRADE') or (TSDict['MODE'] == 'SIMULATION'):
    return False
  else:
    return True

def is_realtime(TSDict):
  if (TSDict['MODE'] == 'TRADE') or (TSDict['MODE'] == 'SIMULATION'):
    return True
  else:
    return False

def is_trade(TSDict):
  if (TSDict['MODE'] == 'TRADE'):
    return True
  else:
    return False
#def logicals_global(string):
#
#  global l_trade
#  global l_realtime
#  global l_backtest
#  #detault option for backtest
#  l_trade = False
#  l_realtime = False
#  l_backtest = True
#  if (string == 'TRADE'): 
#    l_trade = True
#    l_realtime = True
#    l_backtest = False
#  if (string == 'SIMULATION'): 
#    l_trade = False
#    l_realtime = True
#    l_backtest = False
  
#  l_trade_open = False
#  RUNNING_MODE = 'TRADE'
#  
#  while True:
#    data = fetch.get_data(lookback='30 m ago GMT')
#    strategies.basicstrategy(data)
#    time.sleep(60)
