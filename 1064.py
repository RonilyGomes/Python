n1 = float(raw_input())
n2 = float(raw_input())
n3 = float(raw_input())
n4 = float(raw_input())
n5 = float(raw_input())
n6 = float(raw_input())


lista = [n1,n2,n3,n4,n5,n6]

i = 0
positivos = []
while (i < len(lista)):
	if(lista[i] > 0):
		positivos.append(lista[i])
	i++
	

i = resultado = 0
while(i < len(positivos)):
	resultado += positivos[i]
	i++
	
media = resultado / len(positivos)
qtde = len(positivos)


print "%d valores positivos" %qtde
print "%.1f" %media