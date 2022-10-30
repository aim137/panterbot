from panterbot.execute.trading_session import trading_session
from panterbot.data.fetch import get_data
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
import ta
import os
from datetime import datetime
import json

#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

def go(TSdict):

  if is_trade(TSdict):
    key = input('Vas a usar dinero real? \n')
    #if (key != 'paga la panter'): return

  outcome_list = trading_session(TSdict)
  print('Losses: '+str(outcome_list.count('loss')))
  print('Wins: '+str(outcome_list.count('profit')))
  compound = 1
  for i in range(len(outcome_list)):
    if (outcome_list[i] == 'loss'): compound *= (1-TSdict['margin_loss'])
    if (outcome_list[i] == 'profit'): compound *= (1+TSdict['margin_profit'])
  print('Profit: '+str((compound-1)*100)+'%')
  return compound

#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

def test(TSdict):
  """ Function to run backtests. It will instanciate
      a Strategy and a Backtest, it will run the Backtest
      and return/save the results. """

  if is_realtime(TSdict):
    print('This function is for tests, not for running in real time')
    return
  
  setup_directory(TSdict)

  CurrentStrategy = strategy_selector(TSdict)
  df = get_data(TSdict)
  bt = Backtest(df,CurrentStrategy,
                cash=TSdict['SESSION']['cash'],
                commission=TSdict['SESSION']['commission'])
  
  tuning = TSdict['STRATEGY']['tuning'].copy()

  if is_optimize(TSdict):
    output = bt.optimize(**tuning)
    bt.plot(filename=tag+'/plot.html')
  else:
    output = bt.run(**tuning)
    bt.plot(filename=tag+'/plot.html')
  #print(output)
  #bt.plot()

  return bt, output
  
#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

def is_realtime(TSdict):
  if (TSdict['SESSION']['mode'] == 'trade') or (TSdict['SESSION']['mode'] == 'simulation'):
    return True
  else:
    return False

def is_backtest(TSdict):
  return not is_realtime(TSdict)

def is_trade(TSdict):
  if (TSdict['SESSION']['mode'] == 'trade'):
    return True
  else:
    return False

def is_optimize(TSdict):
  if (TSdict['SESSION']['submode'] == 'optimize'):
    return True
  else:
    return False

def setup_directory(TSdict):
  global tag
  tag = datetime.today().strftime('%Y%m%d-%H.%M.%S')
  os.system('mkdir '+str(tag))
  with open(str(tag)+'/input','w') as f:
    for k in TSdict:
      f.write('key: '+str(k)+'\n')
      f.write(json.dumps(TSdict[k]))
      f.write('\n')

#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

def strategy_selector(TSdict):
  """ Function to load the chosen strategy """

  if (TSdict['STRATEGY']['name'] == 'basic'):
    from panterbot.strategies.basic import seektrade as CurrentStrategy
  
  
  if (TSdict['STRATEGY']['name'] == 'macd_ema'):
    from panterbot.strategies.macd_ema import Strat_Macd_Ema as CurrentStrategy
    print('Imported strategy: '+TSdict['STRATEGY']['name'])
    return CurrentStrategy
  
  if (TSdict['STRATEGY']['name'] == 'quick_reversal'):
    from panterbot.strategies.quick_reversal import Quick_Reversal as CurrentStrategy
    print('Imported strategy: '+TSdict['STRATEGY']['name'])
    return CurrentStrategy
  
  if (TSdict['STRATEGY']['name'] == 'sma_cross'):
    from panterbot.strategies.sma_cross import Sma_Cross as CurrentStrategy
    print('Imported strategy: '+TSdict['STRATEGY']['name'])
    return CurrentStrategy
