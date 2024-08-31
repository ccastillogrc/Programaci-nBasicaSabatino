vocales = ["a","e","i","o","u"]
cont=0
texto = input("teclea una palabra o frase")
texto = texto.lower()
for letter in texto :
    if letter in vocales:
        cont += 1
print(cont)
