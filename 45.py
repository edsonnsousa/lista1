quantia = input("Valor requisitado: ")
nota50 =  (quantia/50)
nota10 =  (quantia%50)/10
nota5  =  ((quantia%50)%10)/5
nota1  =  (((quantia%50)%10)%5)/1
print  ("%d Notas de R$ 50|%d Notas de R$ 10|%d Notas de R$ 5|%d Notas de R$ 1" %(nota50,nota10,nota5,nota1))
