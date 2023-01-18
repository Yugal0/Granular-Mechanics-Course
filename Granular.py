import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.stats import norm
from scipy.integrate import trapezoid
import math
df = pd.read_excel("C:/Users/admin/hello/coordinates.xls",sheet_name="fd")
D=df['D']
f=df['f']  #least f
dt = np.repeat(D,f*10000)  #ungrouped data of all the particles (assuming )
print(dt)
domain=np.linspace(np.min(dt),np.max(dt))
fn=norm.pdf(domain,dt.mean(),dt.std())
print("mean ",dt.mean())
print("std ",dt.std())
plt.plot(domain,fn)
plt.hist(dt,bins = 15, density=True )
plt.ylabel("Number fraction")
plt.xlabel("Diameter(micro-meter)")
plt.title("Normal distribution fitted over given data")
plt.text(50,0.08,("mean:",dt.mean(),"std:",(dt.std())))

Vavg=trapezoid((1/6)*math.pi*domain**3*fn,domain)
Dv=((Vavg*6)/(math.pi))**(1/3)
Savg=trapezoid(math.pi*domain**2*fn,domain)
Ds=(Savg/(math.pi))**(1/2)
print(Vavg, Savg) 
print("Dv ",Dv," Ds ",Ds)


cum=np.zeros(D.size)
j=0 #just iterator
for frac in f:
    cum[j]=cum[j-1]+frac
    j+=1
print(cum)
plt.figure(2)
plt.plot(D,cum)
plt.ylabel("Cummulative undersize fraction")
plt.xlabel("Diameter(micro-meter)")
plt.title("Cummulative undersize distribution")
plt.show()   
