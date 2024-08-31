lista1 = []
n=int(input("ingresa un numero"))
lista1.append(n)
n=int(input("ingresa otro numero o teclee 0 para obtener la suma"))
lista1.append(n)
while n != 0:
    n=int(input("ingresa otro numero o teclee 0 para obtener la suma"))
    lista1.append(n)
print(sum(lista1))
