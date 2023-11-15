from panterbot.data.fetch import get_data
from panterbot.driver import strategy_selector


param={
      'SESSION':{
                'mode':'simulation',
                },
      'STRATEGY':{
                 'name':'sma_cross',
                 'tuning':{
                          'n1':50,
                          'n2':200,
                          'sl':0.97,
                          }
                 },
      'DATA':{
             'coin':'ETHGBP',
             'interval':'5m',
             'start_date':'5 min ago GMT'
             }
      }


CurrentStrategy = strategy_selector(param)
df = get_data(param,override_date='1 day ago GMT')

