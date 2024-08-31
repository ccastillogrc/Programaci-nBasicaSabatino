a=0
b=1
n=int(input("ingrese un numero entre 1 y 50"))
while n not in range (1,50):
    print("el numero no esta en el rango")
    n=int(input("ingrese un numero entre 1 y 50"))
for i in range (0,n):
    c=a+b
    a=b
    b=c
    print (b)

                
 
