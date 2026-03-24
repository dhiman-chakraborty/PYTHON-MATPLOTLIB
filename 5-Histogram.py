import matplotlib.pyplot as plt
import numpy as np

# Histogram 1

data = np.random.randint(1,100,size=50)

plt.hist(data,bins=50,color='yellow',edgecolor='black')
plt.title('Histogram chart 1')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()


# Histogram 2

data2 = np.random.randn(100)

plt.hist(data2,bins=50,color='orange',edgecolor='black')
plt.title('Histogram chart 2')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()