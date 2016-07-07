#Definir tempo a partir dos segundos
segundos=int(input("Segundos: "))
hora = (segundos/3600)
minutos = (segundos/60)%60
segundo = (segundos%60)
print ("%d Horas |%d minutos|%d segundos"%(hora,minutos,segundo))
