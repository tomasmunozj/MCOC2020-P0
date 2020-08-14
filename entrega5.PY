from time import perf_counter
import matplotlib.pyplot as plt
from numpy import zeros, float32
import numpy as np
from scipy import linalg

Ns=[1,5,10,20,50,100,200,500,1000,2000,5000,10000]
Nst=[10,20,50,100,200,500,1000,2000,5000,10000,20000]
    
listay3=[0.1e-3,1e-3,1e-2,0.1,1.,10.,60,60*10]
listay2=["0.1 ms","1 ms","10 ms","0.1 s","1 s","10 s","1 min","10 min"]
    
listay5=[10**3,10**4,10**5,10**6,10**7,10**8,10**9,10**10,]
listay4=["1 KB","10 KB","100 KB","1 MB","10 MB","100 MB","1 GB","10 GB","100 GB"]
    
dts=[]
dtsf=[]
Ncorridas=1

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
            
        A=matriz_laplaciana(N,dtype=float32)
        b=np.ones(N)
    
        t1 = perf_counter()
        A_inv=linalg.inv(A)
        A_invb=A_inv@b
        t2 = perf_counter()
            
        dt = t2 - t1
        
        dts2.append(dt) 
    
        print(f"Tiempo transcurrido = {dt} s")       
    dts.append(dts2)   
print (dts) 


for i in range(Ncorridas)   :
    dts3=[]
    
    for N in Ns:
        print (f"N={N}")
            
        A=matriz_laplaciana(N,dtype=float32)
        b=np.ones(N)
    
        t1 = perf_counter()
        A_inv=linalg.solve(A,b)
        t2 = perf_counter()
            
        dt = t2 - t1
        
        dts3.append(dt) 
    
        print(f"Tiempo transcurrido = {dt} s")       
    dtsf.append(dts3)   
print (dtsf) 

           
plt.figure()
plt.subplot(2,1,1)
plt.loglog(Ns,dtsf[0],"-o",color="green",label="linalg.inv")
plt.loglog(Ns,dts[0],"-o",color="red",label="linalg.solve")
plt.ylabel("tiempo transcurrido ")
plt.xlabel("tamaño de la matriz N ")
plt.xticks(Nst,Nst,rotation=45)
plt.grid(True)
plt.yticks(listay3,listay2)
plt.title("Rendimiento A@B")  
 
plt.legend()
plt.tight_layout()
plt.savefig("filename.png",dpi=500)












    