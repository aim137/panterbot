from panterbot import driver as panter

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
                          'take_profit':1.1,
                          'stop_loss':0.98,
                          }
                 },
      'DATA':{
             'coin':'ETHGBP',
             'interval':'4h',
             'start_date':'360 day ago GMT'
             }
      }

backtest,results = panter.test(param)
print(results)
print(results._strategy)
