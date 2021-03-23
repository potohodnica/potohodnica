import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
# f = open(os.path.join(__location__, 'bundled-resource.jpg'))
df = pd.read_csv(os.path.join(__location__, 'hd19.dat'), delimiter="\s+") 
colspecs = [(1, 5), (6, 10), (11, 24), (25, 31), (31, 36)]
#df2 = pd.read_fwf("abs_crte.txt",header=None, colspecs=colspecs,) 

#df3 = df2[(df2.iloc[:,0] == 1000)]
#print(df3)
a = df.iloc[:,0].values + 153
b = df.iloc[:,1].values 
plt.figure(figsize=(15,5))
plt.plot(a, b, c='red')
c = argrelextrema(b, np.less, order=500)

print(b)
plt.scatter(a[c],b[c], c='blue')
plt.title("HD159876")


# plt.axvline(x=[3835]) # HI
# plt.axvline(x=[3889]) # HI

# plt.axvline(x=[3970]) # HI
# plt.axvline(x=[4100]) # HI
# plt.axvline(x=[4226]) # CaI
# plt.axvline(x=[4340]) # HI

# plt.axvline(x=[4860]) # HI
# plt.axvline(x=[5167]) # FeII
# plt.axvline(x=[5890]) # NaI
# plt.axvline(x=[6563]) # HII
# plt.axvline(x=[6868]) # O2
# plt.axvline(x=[7606]) # O2
# plt.axvline(x=[8541]) # HI
# plt.axvline(x=[8660]) # HI


# plt.vlines(df3.iloc[:10,2], ymin=0, ymax=1, linewidth=1, color='g')
# plt.xlim(5885, 5900)
# plt.xlim(5735, 5750)
plt.xlabel('Valovna dolžina (Å)')
plt.ylabel('Intenziteta')
from sklearn.metrics import auc
print('computed AUC using sklearn.metrics.auc: {}'.format(auc(a,b)))
plt.show()