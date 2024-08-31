n=int(input("ingresa un numero entre 1 y 20: "))
while n not in range (1,20):
    print("el numero no esta dentro del rango")
    n=int(input("ingresa un numero entre 1 y 20: "))
if n >=0:
    x = 1
    f = 1
    while x <= n:
        f = f*x
        x += 1
    print ("Eñ factorial de ",n," e:",f)
