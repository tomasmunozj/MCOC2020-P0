from time import perf_counter
import numpy as np
from scipy.sparse import lil_matrix
from numpy import *
from matplotlib import pyplot as plt



Ns=array([1,5,10,20,50,100,200,500,1000,2000,5000])
Nsa=Ns[-1]


Nst=[10,20,50,100,200,500,1000,2000,5000,10000]
Nsx=[10,20,50,100,200,500,1000,2000]
Nsy=[100,200,500,1000,2000]
    
listay3=[0.1e-4,0.1e-3,1e-3,1e-2,0.1,1.,10.,60,60*10]
listay2=["0.01 ms","0.1 ms","1 ms","10 ms","0.1 s","1 s","10 s","1 min","10 min"]
    
dts=[]
dts1=[]
Ncorridas=4

def matriz_laplaciana_llena(N, dtype=np.double):
    
    A = np.identity(N,dtype)*2
    
    for i in range (N):
        
        for j in range (N):
            
            if i+1 == j:
                A[i,j] = -1            
                
            if i-1 == j:
                A[i,j] = -1
                
    return A

for i in range(Ncorridas)   :
    dts2=[]
    dts3=[]
      
    for N in Ns:
        print (f"N={N}")
           
        t1 = perf_counter()
        
        A=matriz_laplaciana_llena(N, dtype=np.double)
        B=matriz_laplaciana_llena(N, dtype=np.double)
            
        t2 = perf_counter()
        
        C = A@B
        
        t3 = perf_counter()
            
        dt = t2 - t1 #tiempo de ensamblado
        dt1 = t3 - t2 #tiempo de solucion 
        
        dts2.append(dt) #agrego los tiempos de ensamblado a la lista
        dts3.append(dt1) #agrego los tiempos de solucion a la lista  
               
        print(f"Tiempo de ensamblado = {dt} s")
        print(f"Tiempo de solucion = {dt1} s")
       
    dts.append(dts2)
    dts1.append(dts3)
    
    hola=array(dts2[-1])
    hola1=array(dts3[-1])


print (dts)
print (dts1)


plt.figure()

plt.subplot(2,1,1)
plt.loglog(Ns,dts[0],"-o",color="grey")
plt.loglog(Ns,dts[1],"-o",color="grey")
plt.loglog(Ns,dts[2],"-o",color="grey")
plt.loglog(Ns,dts[3],"-o",color="grey")
plt.loglog(Ns,Ns**0*(hola),"--")
plt.loglog(Ns,Ns*(hola/Nsa),"--",color="orange")
plt.loglog(Ns,(Ns**2*(hola/(Nsa**2))),"--",color="green")
plt.loglog(Ns,(Ns**3*(hola/(Nsa**3))),"--",color="red")
plt.loglog(Ns,Ns**4*(hola/(Nsa**4)),"--",color="violet")
plt.ylabel("tiempo de ensamblado ")
plt.xticks(Nst,[])
plt.yticks(listay3,listay2)
plt.title(" MATMUL, MATRIZ LLENA")  
plt.ylim([0.00001,300])
      
plt.subplot(2,1,2)
plt.loglog(Ns,dts1[0],"-o",color="grey")
plt.loglog(Ns,dts1[1],"-o",color="grey")
plt.loglog(Ns,dts1[2],"-o",color="grey")
plt.loglog(Ns,dts1[3],"-o",color="grey")

plt.loglog(Ns,Ns**0*(hola1),"--",label="constante")
plt.loglog(Ns,Ns*(hola1/Nsa),"--",color="orange",label="O(N)")
plt.loglog(Ns,Ns**2*(hola1/Nsa**2),"--",color="green",label="O(N2)")
plt.loglog(Ns,Ns**3*(hola1/Nsa**3),"--",color="red",label="O(N3)")
plt.loglog(Ns,Ns**4*(hola1/Nsa**4),"--",color="violet",label="O(N4)")
plt.ylabel("tiempo de solucion")
plt.xlabel("tamaño de la matriz N")
plt.yticks(listay3,listay2)
plt.xticks(Nst,Nst,rotation=45)
plt.ylim([0.00001,30])


plt.legend()
plt.tight_layout()
plt.savefig("MATMUL M LLENA.png",dpi=500)