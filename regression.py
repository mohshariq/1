
#%matplotlib inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize']=(20.0,10.0)

#Reading Data
data=pd.read_csv('headbrain.csv')
print(data.shape)
#print(data.head())

#collecting x and y
X=data['Head Size(cm^3)'].values
Y=data['Brain Weight(grams)'].values

#calculating mean of x and y

mean_x=np.mean(X)
mean_y=np.mean(Y)

m=len(X)

#Using the formula to calculate x and y
n=0
d=0
for i in range(m):
   n=n+(X[i]-mean_x)*(Y[i]-mean_y)
   d=d+(X[i]-mean_x)**2

#printing coefficient
b1=n/d
b0=mean_y-(b1*mean_x)
print(b0,b1)


#Plotting Values and Regression Line

max_x=np.max(X)+100
min_x=np.min(X)-100

#calculating line values x and y
x=np.linspace(min_x,max_x,1000)
y=b0+b1*x

#Plotting Line
plt.plot(x,y,color='#58b970',label='Regresssion Line')

#Plotting Scatter
plt.scatter(X,Y,color='#ef5423',label='Scatter Plot')


plt.xlabel('Head Size in cm3')
plt.ylabel('Brain Weight in grams')
plt.legend()
plt.show()


#Calculating Root Mean squares Error
rmse=0
for i in range(m):
    y_pred=b0+b1*X[i]
    rmse=rmse+(Y[i]-y_pred)**2

rmse=np.sqrt(rmse/m)
print(rmse)


#claculting R value
#r=1-ss_t/ss_r

ss_t=0
ss_r=0

for i in range(m):
    y_pred=b0+b1*X[i]
    ss_t=ss_t+(Y[i]-mean_y)**2
    ss_r=(Y[i]-y_pred)**2

r2=1-(ss_r/ss_t)

print(r2)













































