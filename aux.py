
def run_strategy(data,TSDict,l_trade_open=False):
  if (TSDict['strategy'] == 'basic'):
    from panterbot.strategies.basic import seektrade as current_strategy 



  return current_strategy(data,TSDict,l_trade_open)
