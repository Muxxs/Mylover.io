#coding=utf-8
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
def runplt():
    plt.figure()
    plt.title("时时彩")
    plt.xlabel('期数')
    plt.ylabel('末尾')
    plt.axis([0,10,0,10])
    plt.grid(True)
    return plt
pl=runplt()


print("hello")
from sklearn.linear_model import LinearRegression
print("hello")
X=[]
Y=[]
y="56819118856"
x=0
for i in y:
    x=x+1
    if int(i) >5 :
        i=int(i)-5
    X.append([x])
    Y.append([int(i)])
print(X,Y)
model=LinearRegression()
model.fit(X,Y)
plt.plot(X,Y,'k.')
print(model.predict([x+1])[0])