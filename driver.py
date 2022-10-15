#start
import time
from panterbot.execute.trading_session import trading_session
#from panterbot.data.fetch import get_data

def go(TSDict):

  if is_trade(TSDict):
    key = input('Vas a usar dinero real? \n')
    #if (key != 'paga la panter'): return

  outcome_list = trading_session(TSDict)
  print('Losses: '+str(outcome_list.count('loss')))
  print('Wins: '+str(outcome_list.count('profit')))
  compound = 1
  for i in range(len(outcome_list)):
    if (outcome_list[i] == 'loss'): compound *= (1-TSDict['margin_loss'])
    if (outcome_list[i] == 'profit'): compound *= (1+TSDict['margin_profit'])
  print('Profit: '+str((compound-1)*100)+'%')
  print(outcome_list)
  return compound
  

def is_realtime(TSDict):
  if (TSDict['MODE'] == 'TRADE') or (TSDict['MODE'] == 'SIMULATION'):
    return True
  else:
    return False

def is_backtest(TSDict):
  return not is_realtime(TSDict)

def is_trade(TSDict):
  if (TSDict['MODE'] == 'TRADE'):
    return True
  else:
    return False
