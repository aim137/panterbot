from panterbot import driver as panter

param={
      'SESSION':{
                'mode':'backtest',
                'submode':'run',
                'cash':1000000,
                'commission':0.0015,
                },
      'STRATEGY':{
                 'name':'quick_reversal',
                 'tuning':{
                          'stop_loss' : 0.97,
                          'take_profit' : 1.045,
                          'delta_t_long' : 10,
                          'delta_t_short' : 5,
                          'short_thrs' : 0.015,
                          'long_thrs' : 0.,
                          }
                 },
      'DATA':{
             'coin':'BTCGBP',
             'interval':'1m',
             'start_date':'9 day ago GMT'
             }
      }

backtest,results = panter.test(param)
print(results)
print(results._strategy)
