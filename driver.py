from panterbot.execute.trading_session import trading_session
from panterbot.data.fetch import get_data
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
import ta

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


def test(TSdict):
  """ Function to run backtests. It will instanciate
      a Strategy and a Backtest, it will run the Backtest
      and return/save the results. """

  if is_realtime(TSdict):
    print('This function is for tests, not for running in real time')
    return
 
  CurrentStrategy = strategy_selector(TSdict)

  df = get_data()

  bt = Backtest(df,CurrentStrategy,cash=TSdict['cash'])
  
  output = bt.run()

  bt.plot()

  return
  

def is_realtime(TSdict):
  if (TSdict['MODE'] == 'TRADE') or (TSdict['MODE'] == 'SIMULATION'):
    return True
  else:
    return False

def is_backtest(TSdict):
  return not is_realtime(TSdict)

def is_trade(TSdict):
  if (TSdict['MODE'] == 'TRADE'):
    return True
  else:
    return False

def strategy_selector(TSdict):
  """ Function to load the chosen strategy """

  if (TSdict['strategy'] == 'basic'):
    from panterbot.strategies.basic import seektrade as CurrentStrategy
  
  
  if (TSdict['strategy'] == 'macd_ema'):
    from panterbot.strategies.macd_ema import Strat_Macd_Ema as CurrentStrategy
    print('Imported strat')
    return CurrentStrategy
