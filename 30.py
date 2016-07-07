minutos=int(input("Minutos: "))
dias= (minutos/1440)

horas= (minutos%1440)/60

minu=((minutos%1440)%60)
print ("%d Dias |%d horas|%d minutos"%(dias,horas,minu))

