import numpy as np
import pandas as pd
from scipy.stats import norm
from matplotlib import pyplot as plt
from hathet import Option

K=360
expiry="20221215"
C=Option("C",K,expiry,1)
P=Option("P",K,expiry,-1)

S=124.35
t=0.23
vola=0.3

print(C.calcPrice(S,t, vola) + P.calcPrice(S,t, vola) - S + K)

#prices vs spot
spots=range(250,500,5)
prices=[C.calcPrice(s,1, vola) for s in spots]
pays=[C.calcpayoff(s) for s in spots]

#plt.plot(spots,pays, spots ,prices)
#plt.show()

#optoinprofit calculator

opt_c=Option("C", 380, None,1)
opt_p=Option("P", 380, None ,1)

opt_c.vola=0.3
opt_p.vola=0.3

#opt_c.calcPrice(362,1/12)
#opt_p.calcPrice(362,1/12)


from brown import browngen

gb=browngen()

sigma=0.35
N=250
S0=100
spots=gb.generate(S0 ,0.,sigma,1,N)
times=np.arange(0,1,1/N)
#plt.plot(times,spots)
#plt.show()

opt=Option("C", S0,None,1)

vola=0.3
prices=[]
deltas=[]
for (t,S) in zip(times, spots):
    price=opt.calcPrice(S,1-t,vola)
    delta=opt.calcDelta(S,1-t, vola)
    prices.append(price)
    deltas.append(delta)

plt.plot(times, np.array(prices))
plt.show()


df= pd.DataFrame({"time":times, "spot":spots})

K=100
def calcPrice(row):
    opt=Option("C", K ,None ,1)
    vola=0.3
    return opt.calcPrice(row.spot, 1-row.time,vola)

df["price"]=df.apply(calcPrice, axis=1)    #soronként