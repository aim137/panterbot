from panterbot import driver as panter
#from panterbot.data.fetch import get_data

param={
      'SESSION':{
                'mode':'backtest',
                'cash':1000000,
                'commission':0.0015,
                },
      'STRATEGY':{
                 'name':'macd_ema'
                 },
      'DATA':{
             'coin':'ETHGBP',
             'interval':'4h',
             'start_date':'360 day ago GMT'
             }
      }

#df=get_data(param)
#print(df)
panter.test(param)
