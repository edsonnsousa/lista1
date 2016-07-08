id_anos= int(input("Digite sua idade em dias: "))
anos = (id_anos/360)
meses = (id_anos%360)/30
dias = ((id_anos%360)%30)
print ("%d anos |%d meses |%d dias |"%(anos,meses,dias))
