import numpy
import pandas
myarray=numpy.array([[1,2,3],[4,5,6]])
rowname=["a","b"]
colname=["f1","f2","f3"]
mydataframe = pandas.DataFrame(myarray, index = rowname, columns=colname)
print(mydataframe)

"""
---------------------------------
"""

import numpy
import pandas
myarray = numpy.array([['a','sandhya',9.6],[4,'shreya',6.5]])
rownames = ['r1','r2']
colnames=['f1','f2','f3']
mydataframe = pandas.DataFrame(myarray, index = rownames, columns=colnames)
print(mydataframe)

"""
---------------------------------
"""



from pandas import read_csv
path='diabetes_dataset.csv'
data=read_csv(path)
print (data.shape)

"""
---------------------------------
"""


from pandas import read_csv
url='diabetes_dataset.csv'
data=read_csv(url)
colnames=['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age','Outcome']
print (data.shape)

"""
---------------------------------
"""
description = data.describe()
print(description)

"""
---------------------------------
a"""

print(data.shape)


"""
---------------------------------
b"""

print(data.head(4))

"""
---------------------------------
c"""

print(data.groupby("Outcome").size())

"""
---------------------------------
4"""

import matplotlib.pyplot as plt
import pandas
from pandas.plotting import scatter_matrix
scatter_matrix(data[['Pregnancies','Glucose']])
plt.show()

"""
---------------------------------
"""

import matplotlib.pyplot as plt
import pandas
from pandas.plotting import scatter_matrix
scatter_matrix(data)
plt.show()
data.hist()

"""
---------------------------------
"""

from sklearn.preprocessing import StandardScaler
import pandas
import numpy
arr=data.values
X=arr[:,0:8]
columnsY=arr[:,8]
scaler=StandardScaler().fit(X)
rescaledX=scaler.transform(X)
numpy.set_printoptions(precision=3)
print(rescaledX[0:2,:])
print(X[0:2,:])

"""
---------------------------------
"""

myarray=numpy.array([1,3,-10,4,5,7,-4,-2,10])
mydataframe = pandas.DataFrame(myarray)
print(mydataframe)

"""
---------------------------------
"""

mydataframe.plot(kind='bar')
plt.show()

"""
---------------------------------
"""

from sklearn import preprocessing
fl_x=mydataframe.values.astype(float)
min_max_scaler=preprocessing.MinMaxScaler()
X_scaled=min_max_scaler.fit_transform(fl_x)
df_normalized=pandas.DataFrame(X_scaled)
print(df_normalized)
df_normalized.plot(kind='bar')
plt.show()

