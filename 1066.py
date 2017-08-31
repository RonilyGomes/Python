lista = []

i = 0
while i < 5:
	numero = int(raw_input())
	lista.append(numero)
	i++

i = pares = impares = positivos = negativos = 0

while(i < len(lista)):
	if(lista[i] % 2 == 0):
		pares++
	elif(lista[i] % 2 != 0):
		impares++
		
	if(lista[i] > 0):
		positivos++
	elif(lista[i] < 0):
		negativos++
	
	i++
	
	
print "%d valor(es) par(es)" %pares
print "%d valor(es) impar(es)" %impares
print "%d valor(es) positivo(s)" %positivos
print "%d valor(es) negativo(s)" %negativos