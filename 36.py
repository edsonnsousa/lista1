id_anos= int(input("Digite sua idade em Anos: "))
id_meses =int(input("Digite sua idade em Meses: "))
id_dias = int(input("Digite sua idade em Dias: "))
anos = (id_anos*360)
meses = (id_meses*30)
dias = (id_dias+meses+anos)
print "Sua idade em dias correspode a:  ",dias
