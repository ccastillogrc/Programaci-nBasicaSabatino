n=int(input("ingresa un número: "))
suma=0
while n>0:
    suma = suma + (n%10)
    n = n//10
print("la suma de los digitos e: ",suma)
