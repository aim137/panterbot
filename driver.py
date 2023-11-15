from panterbot.execute.trading_session import trading_session
from panterbot.execute.trading_session import TradingSession
from panterbot.auxlib.functions import *
from panterbot.data.fetch import get_data
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
import ta

#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

def go(TSdict):

  if is_trade(TSdict):
    key = input('Vas a usar dinero real? \n')
    #if (key != 'paga la panter'): return

  df_init = get_data(TSdict,override_date='1 day ago GMT')
  CurrentStrategy = strategy_selector(TSdict)
  ts = TradingSession(df_init,CurrentStrategy)
  ts.run(TSdict)

  return

#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

def test(TSdict):
  """ Function to run backtests. It will instanciate
      a Strategy and a Backtest, it will run the Backtest
      and return/save the results. """

  if is_realtime(TSdict):
    print('This function is for tests, not for running in real time')
    return
  
  tag = setup_directory(TSdict)

  CurrentStrategy = strategy_selector(TSdict)
  df = get_data(TSdict)
  bt = Backtest(df,CurrentStrategy,
                cash=TSdict['SESSION']['cash'],
                commission=TSdict['SESSION']['commission'])
  
  tuning = TSdict['STRATEGY']['tuning'].copy()

  if is_optimize(TSdict):
    output = bt.optimize(**tuning)
 #  bt.plot(filename=tag+'/plot.html')
  else:
    output = bt.run(**tuning)
 #  bt.plot(filename=tag+'/plot.html')
  with open (tag+'/output','w') as f:
   f.write(output.__repr__())
  #bt.plot()

  return bt, output
  
