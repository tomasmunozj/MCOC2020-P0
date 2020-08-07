from scipy import rand
from time import perf_counter
import matplotlib.pyplot as plt

 
Ns=[1,5,10,20,50,100,200,500,1000,2000,5000,10000,20000]
Nst=[10,20,50,100,200,500,1000,2000,5000,10000,20000]
    
listay3=[0.1e-3,1e-3,1e-2,0.1,1.,10.,60,60*10]
listay2=["0.1 ms","1 ms","10 ms","0.1 s","1 s","10 s","1 min","10 min"]
    
listay5=[10**3,10**4,10**5,10**6,10**7,10**8,10**9,10**10,]
listay4=["1 KB","10 KB","100 KB","1 MB","10 MB","100 MB","1 GB","10 GB","100 GB"]
    
dts=[]
mem=[]
Ncorridas=4
for i in range(Ncorridas)   :
    dts2=[]
    mem2=[]
    
    for N in Ns:
        print (f"N={N}")
            
        A = rand(N,N)
        B = rand(N,N)
            
        t1 = perf_counter()
        C = A@B
        t2 = perf_counter()
            
        dt = t2 - t1
        size = 3*(N**2)*8
            
        mem.append(size)
        dts2.append(dt) 
          
              
        print(f"Tiempo transcurrido = {dt} s")
        print(f"Uso memoria = {size}")
        
    dts.append(dts2)
    mem.append(mem2)
print (dts)
       
plt.figure()

plt.subplot(2,1,1)
plt.loglog(Ns,dts[0],"-o",color="blue")
plt.loglog(Ns,dts[1],"-o",color="yellow")
plt.loglog(Ns,dts[2],"-o",color="green")
plt.loglog(Ns,dts[3],"-o",color="red")
plt.ylabel("tiempo transcurrido ")
plt.grid(True)
plt.xticks(Nst,[])
plt.yticks(listay3,listay2)
plt.title("Rendimiento A@B")  
 
        
plt.subplot(2,1,2)
plt.loglog(Ns,mem[0],"-o",color="blue")
plt.ylabel("Uso de memoria")
plt.xlabel("tamaño de la matriz N")
plt.yticks(listay5,listay4) 
plt.grid(True)
plt.xticks(Nst,Nst,rotation=45)
plt.axhline(y=9900000000, xmin=0.001, xmax=0.9999,color="black",ls="--")
    
plt.tight_layout()







    