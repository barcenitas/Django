import random
numero = int(input("Dígame el numero: "))
ran=0
while ran != numero:
	ran=random.randint(1,9)

	if ran == numero:
		print("bien adivinado")
	else:
		print("no has adivinado")
		numero = int(input("Dígame el numero: "))
print(ran)