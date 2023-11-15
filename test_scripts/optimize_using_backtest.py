from panterbot import driver as panter

param={
      'SESSION':{
                'mode':'backtest',
                'submode':'optimize',
                'cash':1000000,
                'commission':0.0015,
                },
      'STRATEGY':{
                 'name':'macd_ema',
                 'tuning':{
                          'take_profit':[1.045,1.03,1.015],
                          'stop_loss':[0.97,0.98,0.99],
                          'maximize':'Return [%]',
                          }
                 },
      'DATA':{
             'coin':'BTCGBP',
             'interval':'15m',
             'start_date':'1 day ago GMT'
             }
      }

backtest,results = panter.test(param)
print(results)
print(results._strategy)
