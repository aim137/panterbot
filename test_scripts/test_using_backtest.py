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
