# Crypto trading bot

This is a python library to backtest strategies in the crypto exchange. It also allows to simulate in real time and to execute orders via the Binance API. However, all of it is under development and must NOT, as of now, be used with real money.
 
This code makes use of libraries such as binance, backtesting, ta, etc.

## Installation


```bash
pip install Backtesting
pip install python-binance
pip install ta
clone repo
cd to repo
pip install -e .
```

## Usage

```python
from panterbot import driver as panter

_lof_tp = [1.02, 1.03, 1.035, 1.04, 1.045, 1.05, 1.055, 1.06]
_lof_tp = [1.065, 1.07, 1.075, 1.08, 1.085, 1.09, 1.095, 1.1]

for tp in _lof_tp:
  param={
        'SESSION':{
                  'mode':'backtest',
                  'submode':'run',
                  'cash':1000000,
                  'commission':0.0015,
                  },
        'STRATEGY':{
                   'name':'macd_ema',
                   'tuning':{
                            'take_profit':tp,
                            'stop_loss':0.98,
                            }
                   },
        'DATA':{
               'coin':'BTCGBP',
               'interval':'5m',
               'start_date':'10 day ago GMT'
               }
        }

  backtest,results = panter.test(param)
  ret = results.to_dict()['Return [%]']
  print(f'{tp}   {ret}')
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

This code belongs in the public domain. You are welcome to take this code and treat is as your own. 
The code is provided "as is" and must NOT be used with real money.

I am not a financial professional and this does not constitute in any way financial advice.
