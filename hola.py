nombre="tomas"
dia=3

print("Forma 1")
print("hola tomas es el 3 de agosto")
print("---------------------------------------------")
print("Forma 2")
print("hola "+nombre+" es el "+str(dia)+" de Agosto")
print("hola "+nombre+" es el "+"3 "+"de Agosto ")
print("---------------------------------------------")
print("Forma 3")
print("hola {nombre} es el {dia} de Agosto".format(dia=dia, nombre=nombre))
print("---------------------------------------------")
print("Forma 4")
print(f"hola {nombre} es el {dia} de Agosto")
#solo en python3
print("---------------------------------------------")
print("Ejemplo 2 -> Forma 1")
print("aloja aloja aloja aloja aloja")
print("---------------------------------------------")
print("Ejemplo 2 -> Forma 2")
print("aloja "*5)
