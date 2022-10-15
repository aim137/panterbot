import panterbot.driver as pb

parametros={
           'MODE':'BACKTEST',
           'strategy':'basic',
           'margin_profit': 0.03,
           'margin_loss': 0.01,
            }

posibles_profits = [0.02, 0.03, 0.04]
posibles_losses = [0.01, 0.005, 0.001]
resultados = []

with open('resultados.txt','w') as f:
  for i_pro in range(len(posibles_profits)):
     for i_los in range(len(posibles_losses)):

       parametros['margin_profit']=posibles_profits[i_pro]
       parametros['margin_loss']=posibles_losses[i_los]

       compind = pb.go(parametros)
       resultados.append(compind)

       f.write('Con profit '+str(posibles_profits[i_pro])+' y loss '+str(posibles_losses[i_los])+' obtuve --> '+str((compind-1)*100)+'%\n')
#counter=0
#for i_pro in range(len(posibles_profits)):
 #   for i_los in range(len(posibles_losses)):
  #     print('<><><><><><><><><><><>')
#    print(i_pro)
 #      print(i_los)
  #     print(resultados[counter])
   #    print('<><><><><><><><><><><>')
    #   counter += 1