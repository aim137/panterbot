import panterbot.driver as pb

parametros={
           'MODE':'BACKTEST',
           'strategy':'basic',
           'margin_profit': 0.03,
           'margin_loss': 0.01,
            }

pb.go(parametros)
