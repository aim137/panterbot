#start
import time
from panterbot.aux import trading_session
from panterbot.data.fetch import get_data

def go(TSDict):

  if is_trade(TSDict):
    key = input('Vas a usar dinero real? \n')
    #if (key != 'paga la panter'): return

  outcome_list = trading_session(TSDict)
  print('Losses: '+str(outcome_list.count('loss')))
  print('Wins: '+str(outcome_list.count('profit')))
  print('Profit: '+str(
                   outcome_list.count('profit')*.15
                  -outcome_list.count('loss')*.15
                      ))
  

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
