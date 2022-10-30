import sys
from binance import Client
import pandas as pd
sys.path.append('/Users/aim/opt/anaconda3/envs/PanterBot/lib/python3.8/site-packages/panterbot/.secrets')
sys.path.append('/home/maria/Panterbot/panterbot/.secrets')
import keys

client = Client(keys.api_key,keys.secret_key)

def get_data(TSdict,override_date=None):
  """ function to get data
  """

  if 'coin' in TSdict['DATA'].keys():
    symbol = TSdict['DATA']['coin']
  else:
    symbol = 'ETHGBP'
  if 'interval' in TSdict['DATA'].keys():
    interval = TSdict['DATA']['interval']
  else:
    interval = '4h'
  if 'start_date' in TSdict['DATA'].keys():
    start_date = TSdict['DATA']['start_date']
  else:
    start_date = '100 day ago GMT'

  if override_date is not None:
    start_date = override_date
    print(f'Getting data for {symbol} in the {interval} time frame since date {start_date}')

  frame = pd.DataFrame(client.get_historical_klines(symbol,interval,start_date))
  frame = frame.iloc[:,:6]
  frame.columns = ['Time','Open','High','Low','Close','Volume']
  frame = frame.set_index('Time')
  frame.index = pd.to_datetime(frame.index, unit='ms')
  frame = frame.astype(float)
  return frame


#datosdelosperis = get_data()
#print(datosdelosperis)
  
