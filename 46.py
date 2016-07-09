valor_merc =  input("Valor da Mercadoria: ")
entrada =  ((valor_merc/3)+ (valor_merc%3))
parcela = (valor_merc - entrada)/2
print ("Entrada :  %.2f || 2 Parcelas: %.2f "%(entrada,parcela))
