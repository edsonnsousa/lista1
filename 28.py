horas=int(input("Horas: "))
mes = (horas/720)

semana = ((horas%720)/168)

dias = ((horas%720)%168)/24

print ("%d Mes |%d semanas|%d dias"%(mes,semana,dias))
