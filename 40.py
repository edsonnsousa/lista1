print "#__Gasto de um fumante__ #"
anos = input("Anos que eh fumante: ")
dia= input("Cigarros por dia: ")
preco= input("Preco do cigarro(Carteira): ")
total= ((anos*360)*dia)*(preco/20)
print "Total gasto: R$ ",total
