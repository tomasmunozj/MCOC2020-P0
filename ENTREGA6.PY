from time import perf_counter
import matplotlib.pyplot as plt
from numpy import zeros, float32
import numpy as np
import scipy.linalg as splinalg
import numpy.linalg as nplinalg



Ns=[1,10,50,100,300,800,1000,2000,3000,4000,5000]
Nst=[10,20,50,100,200,500,1000,2000,5000,10000,20000]
    
listay3=[0.1e-3,1e-3,1e-2,0.1,1.,10.,60,60*10]
listay2=["0.1 ms","1 ms","10 ms","0.1 s","1 s","10 s","1 min","10 min"]
    
dts=[]
dtsf=[]
dtsf1=[]
dtsf2=[]
dtsf3=[]
dtsf4=[]
Ncorridas=1

def matriz_laplaciana(N, dtype=float32):
    
    A = zeros((N,N), dtype=float32)
    
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
        A_inv=splinalg.inv(A)
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
        A_inv=splinalg.solve(A,b)
        t2 = perf_counter()
            
        dt = t2 - t1
        
        dts3.append(dt) 
    
        print(f"Tiempo transcurrido = {dt} s")       
    dtsf.append(dts3)   
print (dtsf) 


for i in range(Ncorridas)   :
    dts4=[]
    
    for N in Ns:
        print (f"N={N}")
            
        A=matriz_laplaciana(N,dtype=float32)
        b=np.ones(N)
    
        t1 = perf_counter()
        A_inv=nplinalg.solve(A,b)
        t2 = perf_counter()
            
        dt = t2 - t1
        
        dts4.append(dt) 
    
        print(f"Tiempo transcurrido = {dt} s")       
    dtsf1.append(dts4)   
print (dtsf1) 

for i in range(Ncorridas)   :
    dts5=[]
    
    for N in Ns:
        print (f"N={N}")
            
        A=matriz_laplaciana(N,dtype=float32)
        b=np.ones(N)
    
        t1 = perf_counter()
        A_inv=splinalg.solve(A,b,sym_pos=False)
        t2 = perf_counter()
            
        dt = t2 - t1
        
        dts5.append(dt) 
    
        print(f"Tiempo transcurrido = {dt} s")       
    dtsf2.append(dts5)   
print (dtsf2) 

for i in range(Ncorridas)   :
    dts6=[]
    
    for N in Ns:
        print (f"N={N}")
            
        A=matriz_laplaciana(N,dtype=float32)
        b=np.ones(N)
    
        t1 = perf_counter()
        A_inv=splinalg.solve(A,b,overwrite_a=False)
        t2 = perf_counter()
            
        dt = t2 - t1
        
        dts6.append(dt) 
    
        print(f"Tiempo transcurrido = {dt} s")       
    dtsf3.append(dts6)   
print (dtsf3) 


for i in range(Ncorridas)   :
    dts7=[]
    
    for N in Ns:
        print (f"N={N}")
            
        A=matriz_laplaciana(N,dtype=float32)
        b=np.ones(N)
    
        t1 = perf_counter()
        A_inv=splinalg.solve(A,b,check_finite=False)
        t2 = perf_counter()
            
        dt = t2 - t1
        
        dts7.append(dt) 
    
        print(f"Tiempo transcurrido = {dt} s")       
    dtsf4.append(dts7)   
print (dtsf4) 
           
plt.figure()
plt.subplot(1,1,1)
plt.loglog(Ns,dtsf[0],"-o",color="green",label="splinalg.solve")
plt.loglog(Ns,dts[0],"-o",color="red",label="splinalg.inv")
plt.loglog(Ns,dtsf1[0],"-o",color="orange",label="nplinalg.solve")
plt.loglog(Ns,dtsf2[0],"-o",color="blue",label="splinalg.solve_symmetric")
plt.loglog(Ns,dtsf3[0],"-o",color="violet",label="splinalg.solve_overwrite")
plt.loglog(Ns,dtsf4[0],"-o",color="brown",label="splinalg.solve_check_finite")
plt.ylabel("tiempo transcurrido ")
plt.xlabel("tamaño de la matriz N ")
plt.xticks(Nst,Nst,rotation=45)
plt.grid(True)
plt.yticks(listay3,listay2)
plt.title("Rendimiento solvers Ax=b")  
 
plt.legend()
plt.tight_layout()
plt.savefig("filename.png",dpi=500)











    