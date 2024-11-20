import random
personas=[{'edad':random.randint(0,65),'sexo':random.choice(['M','F'])} for _ in range(50)]
for p in personas:print(p)
mayores=sum(1 for p in personas if p['edad']>=18)
menores=sum(1 for p in personas if p['edad']<=17)
masculinos_mayores=sum(1 for p in personas if p['edad']>=18 and p['sexo']=='M')
femeninas_menores=sum(1 for p in personas if p['edad']<=17 and p['sexo']=='F')
porc_mayores=(mayores/50)*100
porc_femeninas=(sum(1 for p in personas if p['sexo']=='F')/50)*100
print('Las personas de 18 años o mas son '+str(mayores))
print('Las personas de 17 años o menos son '+str(menores))
print('Las personas masculinas de 18 años o mas son '+str(masculinos_mayores))
print('Las personas femeninas de 17 años o menos son '+str(femeninas_menores))
print('Las personas de 18 años o mas son el '+str(porc_mayores)+'% del total')
print('Las personas femeninas son el '+str(porc_femeninas)+'% del total')