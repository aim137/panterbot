import pandas as pd
import fetch

def basicstrategy(data_frame):
  """ Basic strategy, 
      accepts pandas dataframe as input
  """
  cumulret = (data_frame.Open.pct_change()+1).cumprod() -1
  if cumulret[-1] < -0.002:
     open_price = cumulret[-1] 
     open_time = data_frame.index[-1]
     print('time = '+str(open_time)+' - OPEN TRADE at price '+str(open_price))
     while True:
       data_for_exit = fetch.get_data(lookback='30 m ago GMT')
       data_since_buy = data_for_exit.loc[data_for_exit.index > open_time]
       if len(data_since_buy) > 0:
         sincebuyreturn = (data_since_buy.Open.pct_change()+1).cumprod() -1
         if sincebuyreturn[-1] > 0.0015:
           print('I made profit')
           break
         if sincebuyreturn[-1] < -0.0015:
           print('I made a loss')
           break
  else:
     print('time = '+str(data_frame.index[-1])+' - no trade has been executed')

