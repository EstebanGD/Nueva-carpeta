#numeros del 0 al 8, en forma de reloj de arena, pero con una diagonal de 8
"""for i in range(8):
    j=i
    while i > 0:
        print(" ", end="")
        i = i-1
    i=j
    for j in range(i,9,+1):
        print(j, end = " ")
    if i != 7:
        print(" ")

for i in range(8,-2,-1):
    j=i
    while i > -1:
        print(" ", end="")
        i = i-1
    i=j
    for j in range(8,i,-1):
        print(j, end = " ")
    print(" ")"""

#Impresion numeros del 1 al 8, similar a un reloj de arena
for i in range(8):
    j=i
    while i > 0:
        print(" ", end="")
        i = i-1
    i=j
    for j in range(i,9,+1):
        print(j, end = " ")
    print(" ")

for i in range(8,-1,-1):
    j=i
    while i > 0:
        print(" ", end="")
        i = i-1
    i=j
    for j in range(i,9,+1):
        print(j, end = " ")
    print(" ")

print("Este es un mensaje añadido en la rama correcciones")
print("El programa funciona correctamente ahora provaremos remover de stagged.")