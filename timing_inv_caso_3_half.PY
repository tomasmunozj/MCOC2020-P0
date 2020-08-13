from time import perf_counter
import matplotlib.pyplot as plt
import sys
from numpy import zeros, float32
import numpy as np


from scipy import linalg


Ns=[1,5,10,20,50,100,200,500,1000,2000,5000]
Nst=[10,20,50,100,200,500,1000,2000,5000,10000,20000]
    
listay3=[0.1e-3,1e-3,1e-2,0.1,1.,10.,60,60*10]
listay2=["0.1 ms","1 ms","10 ms","0.1 s","1 s","10 s","1 min","10 min"]
    
listay5=[10**3,10**4,10**5,10**6,10**7,10**8,10**9,10**10,]
listay4=["1 KB","10 KB","100 KB","1 MB","10 MB","100 MB","1 GB","10 GB","100 GB"]
    
dts=[]
mem=[]
Ncorridas=10

def matriz_laplaciana(N, dtype=float32):
    
    A = zeros((N,N), dtype=np.half)
    
    for i in range (N):
        
        for j in range (N):
            
            if i==j:
                A[i,j]=2
                
            if i+1==j:
                A[i,j]=-1
                
            if i-1==j:
                A[i,j]=-1
                
    return A

for i in range(Ncorridas)   :
    dts2=[]
      
    for N in Ns:
        print (f"N={N}")
            
        a=matriz_laplaciana(N,dtype=float32)
    
            
        t1 = perf_counter()
        
        M_inv=linalg.inv(a,overwrite_a=True)
        
        t2 = perf_counter()
            
        dt = t2 - t1
        
        dts2.append(dt) 
                               
        print(f"Tiempo transcurrido = {dt} s")
       
    dts.append(dts2)
   
print (dts)
print (mem)  
 

for N in Ns:
    A=matriz_laplaciana(N)
    size = (sys.getsizeof(A))
    mem.append(size)
    print(f"Uso memoria = {size}")
           
plt.figure()

plt.subplot(2,1,1)
plt.loglog(Ns,dts[0],"-o",color="blue")
plt.loglog(Ns,dts[1],"-o",color="goldenrod")
plt.loglog(Ns,dts[2],"-o",color="yellow")
plt.loglog(Ns,dts[3],"-o",color="aqua")
plt.loglog(Ns,dts[4],"-o",color="red")
plt.loglog(Ns,dts[5],"-o",color="orange")
plt.loglog(Ns,dts[6],"-o",color="greenyellow")
plt.loglog(Ns,dts[7],"-o",color="green")
plt.loglog(Ns,dts[8],"-o",color="pink")
plt.loglog(Ns,dts[9],"-o",color="slateblue")
plt.ylabel("tiempo transcurrido ")
plt.xticks(Nst,[])
plt.grid(True)
plt.yticks(listay3,listay2)
plt.title("Rendimiento A@B")  
 
        
plt.subplot(2,1,2)
plt.loglog(Ns,mem,"-o")
plt.ylabel("Uso de memoria")
plt.xlabel("tamaño de la matriz N")
plt.yticks(listay5,listay4) 
plt.grid(True)
plt.xticks(Nst,Nst,rotation=45)
plt.axhline(y=5000000000, xmin=0.001, xmax=0.9999,color="black",ls="--")
    
plt.tight_layout()












    