import pandas as pd
import panterbot.driver as pb
from panterbot.data.fetch import get_data

def seektrade(data_frame,TSDict,l_trade_open=False):
  """ Basic strategy, 
      accepts pandas dataframe as input
  """

  if (not l_trade_open):
    cumulret = (data_frame.Open.pct_change()+1).cumprod() -1
    if cumulret[-1] < -0.002:
      global open_price
      global open_time
      open_price = cumulret[-1] 
      open_time = data_frame.index[-1]
      print('time = '+str(open_time)+' - OPEN TRADE at price '+str(open_price))
      #crear objeto trade
       
      if (pb.is_realtime(TSDict)):
        while True:
          data_for_exit = get_data(lookback='30 m ago GMT')
          data_since_buy = data_for_exit.loc[data_for_exit.index > open_time]
          if len(data_since_buy) > 0:
            sincebuyreturn = (data_since_buy.Open.pct_change()+1).cumprod() -1
            if sincebuyreturn[-1] > 0.0015:
              print('I made profit')
              break
            if sincebuyreturn[-1] < -0.0015:
              print('I made a loss')
              break

      if (pb.is_backtest(TSDict)):
        return True
    else:
      print('time = '+str(data_frame.index[-1])+' - no trade has been executed')
  else: #this is only for backtesting
    l_should_exit, result = check_exit(open_time)
    print('I made '+result)
    return l_should_exit

def check_exit(open_time):
 data_for_exit = get_data(lookback='30 m ago GMT')
 data_since_buy = data_for_exit.loc[data_for_exit.index > open_time]
 if len(data_since_buy) > 0:
   sincebuyreturn = (data_since_buy.Open.pct_change()+1).cumprod() -1
   if sincebuyreturn[-1] > 0.0015:
     result = 'profit'
     return True, result
   if sincebuyreturn[-1] < -0.0015:
     result = 'loss'
     return True, result
