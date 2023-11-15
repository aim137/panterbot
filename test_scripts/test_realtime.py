from panterbot import driver as panter

param={
      'SESSION':{
                'mode':'simulation',
                },
      'STRATEGY':{
                 'name':'rt_sma_cross',
                 'tuning':{
                          'n1':50,
                          'n2':200,
                          'sl':0.97,
                          }
                 },
      'DATA':{
             'coin':'ETHGBP',
             'interval':'5m',
             'start_date':'5 m ago GMT'
             }
      }

panter.go(param)
