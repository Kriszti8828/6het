import numpy as np
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

plt.plot(spots,pays, spots ,prices)
plt.show()

#optoinprofit calculator

