lista=[]
cant=int(input("¿Cuantos números desea ingresar?"))
i=1
while i <= cant:
    n=int(input("ingree un número: "))
    lista.append(n)
    i+=1
print("número mayor: ",max(lista))
print("número menor: ",min(lista))
