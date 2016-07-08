numero = int(input("Digite o Numero"))
m=(numero/1000)
c=(numero%1000)/100
d=((numero%1000)%100)/10
u =((numero%1000)%100)%10
soma = m+c+d+u
print "Soma: ",soma
