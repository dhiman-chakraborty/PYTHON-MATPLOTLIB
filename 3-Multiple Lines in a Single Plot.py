import matplotlib.pyplot as plt

x = [10,20,30,40,50,60]
y1 = [1200,3211,1622,756,2011,4522]
y2 = [5622,452,6387,1002,842,3689]

plt.plot(x,y1,color='red',linestyle='--',linewidth=3,marker='o',markersize=10,label='Red Line')      # label: name for legend
plt.plot(x,y2,color='green',linestyle='--',linewidth=3,marker='o',markersize=10,label='Green Line')
plt.title('Multiple line in single plot chart')
plt.xlabel('x-plot')
plt.ylabel('y-plot')
plt.legend(loc='best')
plt.grid(True)
plt.show()