from scipy import rand
from time import perf_counter
import matplotlib.pyplot as plt

Ns=[1,5,10,20,50,100,200]
Nst=[10,20,50,100,200,500,1000,2000,5000,10000,20000]
    
listay3=[0.1e-3,1e-3,1e-2,0.1,1.,10.,60,60*10]
listay2=["0.1 ms","1 ms","10 ms","0.1 s","1 s","10 s","1 min","10 min"]
    
listay5=[10**3,10**4,10**5,10**6,10**7,10**8,10**9,10**10,]
listay4=["1 KB","10 KB","100 KB","1 MB","10 MB","100 MB","1 GB","10 GB","100 GB"]
    
dts=[]
mem=[]
Ncorridas=10

def mimatmul(A,B):
    c = []
    
    for i in range(0,len(A)):
        inicio=[]
        
        for j in range(0,len(B[i])):
            resultado = 0
            
            for k in range(0,len(A[i])):
                resultado += A[i][k]*B[k][j]
                
        inicio.append(resultado)
        
    c.append(inicio)

    return c

for i in range(Ncorridas)   :
    dts2=[]
      
    for N in Ns:
        print (f"N={N}")
            
        A = rand(N,N)
        B = rand(N,N)
            
        t1 = perf_counter()
        C = mimatmul(A,B) 
        t2 = perf_counter()
            
        dt = t2 - t1
        
        dts2.append(dt) 
                               
        print(f"Tiempo transcurrido = {dt} s")
       
    dts.append(dts2)
   
print (dts)
print (mem)  
 

for N in Ns:
    A = rand(N,N)
    B = rand(N,N)
    size = 3*(N**2)*8
    mem.append(size)
    print(f"Uso memoria = {size}")
           
plt.figure()

plt.subplot(2,1,1)
plt.loglog(Ns,dts[0],"-o",color="blue")
plt.loglog(Ns,dts[1],"-o")
plt.loglog(Ns,dts[2],"-o",color="yellow")
plt.loglog(Ns,dts[3],"-o",color="aqua")
plt.loglog(Ns,dts[4],"-o",color="red")
plt.loglog(Ns,dts[5],"-o",color="orange")
plt.loglog(Ns,dts[6],"-o",color="greenyellow")
plt.loglog(Ns,dts[7],"-o",color="green")
plt.loglog(Ns,dts[8],"-o",color="pink")
plt.loglog(Ns,dts[9],"-o",color="slateblue")
plt.ylabel("tiempo transcurrido ")
plt.grid(True)
plt.xticks(Nst,[])
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

plt.savefig("filename.png",dpi=500)







    