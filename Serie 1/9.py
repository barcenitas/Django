numero = int(input("Dígame el numero: "))
numero_aumento=numero
factorial = 1
i = 1
if numero==int(0):
	print(0)
else:
	while i <= numero_aumento:
		factorial = factorial * i
		i = i + 1
	print(factorial)