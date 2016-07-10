# -*- coding: cp1252 -*-
print "#_Questionario Investigativo_#"
print "digite 's'para SIM||digite 'n'para NAO"
status=0
q1 =  raw_input("Telefonou para a vítima ?")
q2 =  raw_input("Esteve no local do crime ?")
q3 =  raw_input("Mora perto da vítima ?")
q4 =  raw_input("Devia para a vítima ?")
q5 =  raw_input("Já trabalhou com a vítima ?")
if  q1 == 's'or q1 == 'S':
    status += 1
else:
    pass
if  q2 == 's' or q2 == 'S':
    status += 1
else:
    pass
if  q3 == 's' or q3 == 'S':
    status += 1
else:
    pass
if  q4 == 's' or q4 == 'S':
    status += 1
else:
    pass
if  q5 == 's' or q5 == 'S':
    status += 1
else:
    pass

print status
if status ==2:
    print "Suspeito"
if status ==3 or  status ==4:
    print "Cumplice"
if status ==5:
    print "Assassino"
if status ==1 or status ==0:
    print  "Inocente"
