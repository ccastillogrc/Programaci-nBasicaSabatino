caracter=[]
cont=0
x = input("ingrese el caracter a buscar")
caracter.append(x)
texto = input("teclea una palabra o frase")
texto = texto.lower()
for letter in texto :
    if letter in x:
        cont += 1
print(cont)
