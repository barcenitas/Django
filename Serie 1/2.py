print("Convertir a Celsius:   [1]")
print("Convertir a Fahrenheit:[2]")
respuesta = int(input("Dígame el numero: "))
if respuesta == 1:
	Fahrenheit = float(input("Dígame el numero a convertir: "))
	c=(Fahrenheit-32)/1.8
	print(c)
else:
	Celsius=float(input("Dígame el numero a convertir: "))
	f=((Celsius)*(1.8))+32
	print(f)