num = int(input("Digite o numero"))
c = num/100
d = (num%100)/10
u = (num%100)%10
uni=str(u)
dez=str(d)
cen=str(c)
inverso = (uni+dez+cen)
contrario = int(inverso)
subtra =int(num-contrario)
print subtra
