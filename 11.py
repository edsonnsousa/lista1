num = int(input("Digite o numero"))
c = num/100
d = (num%100)/10
u = (num%100)%10

print"ordem de entrada",num
print "Ordem inversa "+"%d"%u + "%d"%d + "%d"%c
