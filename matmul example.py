import scipy as sp
#Matriz forma1
A=sp.rand(2,2)
print (A)
print("-------------------------------")
#Matriz forma2
N=2
B=sp.rand(N,N)
print (B)
print("-------------------------------")
#Matriz forma3
C=sp.rand(N,N)
print (f"C = {C}")
print("-------------------------------")
#Matriz forma 4
print (f"C = \n{C}")
print("-------------------------------")
#ahora ojo con numpy, ya que esto es una multiplicacion de arreglos
D=A*B
print (f"D = \n{D}")
