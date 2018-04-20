cadena =input("Dígame la palabra: ")
lista=list(cadena)

print("inicio")
for letra in lista:    
   if letra == 'a' or letra== 'e' or letra== 'i' or letra== 'o' or letra== 'u':
      continue
   print (letra)
print("fin")