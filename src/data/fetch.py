import sys
from binance import Client
import pandas as pd
sys.path.append('/Users/aim/idea/panterbot/.secrets')
import keys

client = Client(keys.api_key,keys.secret_key)

def get_data(symbol='BTCUSDT',interval='1m',lookback='30 m ago GMT'):
  """ function to get data
  """

  frame = pd.DataFrame(client.get_historical_klines(symbol,interval,lookback))
  frame = frame.iloc[:,:6]
  frame.columns = ['Time','Open','High','Low','Close','Volume']
  frame = frame.set_index('Time')
  frame.index = pd.to_datetime(frame.index, unit='ms')
  frame = frame.astype(float)
  return frame


#datosdelosperis = get_data()
#print(datosdelosperis)
  
