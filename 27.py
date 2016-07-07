segundos=int(input("Segundos: "))
hora = (segundos/3600)
minutos = (segundos/60)%60
segundo = (segundos%60)
print (hora,"Horas ,%d minutos,%d segundos"%minutos %segundo)
print minutos
print segundo
