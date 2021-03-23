import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema

df = pd.read_csv("HD16_trimmed_prviVrh.dat", delimiter="\s+") 
# df = pd.read_csv("HD16_trimmed_drugiVrh.dat", delimiter="\s+") 
colspecs = [(1, 5), (6, 10), (11, 24), (25, 31), (31, 36)]
#df2 = pd.read_fwf("abs_crte.txt",header=None, colspecs=colspecs,) 

#df3 = df2[(df2.iloc[:,0] == 1000)]
#print(df3)
a = df.iloc[:,0].values + 2.4
b = df.iloc[:,1].values
plt.figure(figsize=(15,5))
plt.plot(a, b, c='red')
c = argrelextrema(b, np.less, order=20)

# print(a[c])
plt.scatter(a[c],b[c], c='blue')
print(b)
plt.title("HD159876")


# plt.vlines(df3.iloc[:10,2], ymin=0, ymax=1, linewidth=1, color='g')
plt.xlim(5885, 5900)
plt.xlabel('Valovna dolžina (Å)')
plt.ylabel('Intenziteta')

from sklearn.metrics import auc
print('computed AUC using sklearn.metrics.auc: {}'.format(auc(a,b)))