numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
i = 0
j = 0

for num in numeros:
	if num%2 == 0:
		print ('este numero es par') 
		i += 1
	if num%2 != 0:
		print ('este numero es inpar') 
		j += 1
print("Programa terminado")
print("Total de num. pares " + str(i))
print("Total de num. impares " + str(j))