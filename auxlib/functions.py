from datetime import datetime
import json
import os

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
  tag = datetime.today().strftime('%Y%m%d-%H.%M.%S')
  os.system('mkdir '+str(tag))
  with open(str(tag)+'/input','w') as f:
    for k in TSdict:
      f.write('key: '+str(k)+'\n')
      f.write(json.dumps(TSdict[k]))
      f.write('\n')
  return tag

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

  if (TSdict['STRATEGY']['name'] == 'rt_sma_cross'):
    from panterbot.strategies.rt_sma_cross import RTSma_Cross as CurrentStrategy
    print('Imported strategy: '+TSdict['STRATEGY']['name'])
    return CurrentStrategy
                                                              
