print("__#Soma de Fracao#__")
nume1=int(input("Digite o numerador "))
deno1=int(input("Digite o denominador "))
print ("Fracao #1 %d/%d"%(nume1,deno1))
nume2=int(input("Digite o numerador "))
deno2=int(input("Digite o denominador "))
print ("Fracao #1 %d/%d"%(nume2,deno2))
if deno1 == deno2:
    soma_deno = (deno1+deno2)
    soma_nume=(nume1+nume2)
    print ("%d/%d"%(soma_deno,soma_nume))
else:
    soma_deno = ((deno1*nume2)+(deno2*nume1))
    soma_nume = ((nume1*nume2))
    print ("%d/%d"%(soma_deno,soma_nume))

