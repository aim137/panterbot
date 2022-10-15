import pandas as pd
import panterbot.driver as pb
from panterbot.data.fetch import get_data

def seektrade(data_frame,TSDict):
  """ Basic strategy, 
      accepts pandas dataframe as input
  """

  cumulret = (data_frame.Open.pct_change()+1).cumprod() -1
  objeto = {'open_price':cumulret[-1],
             'open_time':data_frame.index[-1]}
  if cumulret[-1] < -0.002:
    print('time = '+str(objeto['open_time'])+' - OPEN TRADE at price '+str(objeto['open_price']))
    #crear objeto trade
    return True, objeto
     
  else:
    print('time = '+str(data_frame.index[-1])+' - no trade has been executed')
    return False,objeto




def seekexit(data_frame,TSDict,objeto):
  
  margin_profit = TSDict['margin_profit']
  margin_loss   = TSDict['margin_loss']

  if pb.is_realtime(TSDict):
    data_for_exit = get_data(lookback='30 m ago GMT')
    data_since_buy = data_for_exit.loc[data_for_exit.index > objeto['open_time']]
  if pb.is_backtest(TSDict):
    data_since_buy = data_frame.loc[data_frame.index > objeto['open_time']]

  if len(data_since_buy) > 0:
    sincebuyreturn = (data_since_buy.Open.pct_change()+1).cumprod() -1
    if (sincebuyreturn[-1] > margin_profit) or (sincebuyreturn[-1] < (-1 * margin_loss)):
      objeto['outcome'] = 'profit'
      if sincebuyreturn[-1] < (-1 * margin_loss): objeto['outcome'] = 'loss'
      print('time = '+str(objeto['open_time'])+' - CLOSE TRADE with '+str(objeto['outcome']))
      return False, objeto
    else:
      return True, objeto
  else:
    return True, objeto
