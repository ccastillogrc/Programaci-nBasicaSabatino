t=input("ingresar texto: ")
i=0
c=1
while i < len(t):
    if t[i] == " ":
        c = c+1
    i = i+1
print(f"El texto tiene {c} palabra.")
