import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#df=pd.DataFrame(data={'A':[3,4,5], 'B':[2,3,5]})
#df['C']=df('A')+df('B')

df=pd.DataFrame(columns=['num', 'fib'])


#sor hozzádása
#append, helyette pd.concat, pd.merge, pd.join
row1={'num':1, 'fib':1}
row2={'num':1, 'fib':1}
new_df=pd.DataFrame([row1, row2])
df=pd.concat([df, new_df], axis=0, ignore_index=True)

#df=pd.append({'num':1, 'fib':1}, ignore_index=True)
print(df)
print(df.dtypes)

df2=pd.DataFrame(range(1,20), columns=['num'], ) #index=range(2,100) meg lehet ezt is adni
df2['fib']=np.nan  #üres adat
print(df2)

#df2.loc[df2['num']==1, 'fib']=1  #elején feltétel, oszlop beállítása
#df2.loc[df2['num']==2, 'fib']=1

#df2.loc[df2['num'] in [1, 2], 'fib']=1  #érték benne van egy adott listában


for ix,row in df2.iterrows(): #végig iterál a dataframen
    if ix in [0,1]:
        #row['fib']=1
        df2.loc[ix, 'fib'] = 1
    else:
        df2.loc[ix,'fib']=df2.loc[ix-1, 'fib']+df2.loc[ix-2, 'fib']
    print(ix)
    print(row)
    print(row['num']) #értékre hivatkozni
print(df2)

import sys

#class (3 paraméter) amiben array- hány sor hány oszlop

class VelSzamok():
    def __init__(self, n_rows, n_cols):
        self.n_rows=n_rows
        self.n_cols=n_cols
        self.value=np.random.random((self.n_rows, self.n_cols))

    def plot_column_avarages(self, show:True):
        averages=self.value.mean(axis=0)
        print(averages)
        plt.plot(averages)
        if show:
            plt.show()


a2=VelSzamok(6000,3)

a1.plot_column_avarages()
