numero = input("Digite o numero: ")
a = (numero/1000)
b = (numero%1000)/100
c = ((numero%1000)%100)/10
d = ((numero%1000)%100)%10
a = a*(2**3)
b = b*(2**2)
c = c*(2**1)
d = d*(2**0)
print a+b+c+d
