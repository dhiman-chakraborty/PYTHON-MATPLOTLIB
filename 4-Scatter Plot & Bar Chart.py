import matplotlib.pyplot as plt

#### Scatter Plot  ####

# Used to visualize relationship between two variables.

x = [10,20,30,40,50,60]
y = [1262,634,961,2033,3025,756]

plt.scatter(x,y,color='blue',marker='*',s=50)
plt.title('Scatter plot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()

# Parameters explained
# color: color of all the points (Name: 'green', 'red', 'blue' | Short code: 'g', 'r', 'b' | HEX code: '#00FF00')
# marker: Defines the shape of each data point ('o' : Circle (default), 's' : Square, 'D' : Diamond, 'p' :Pentagon, '*' : Star, '+', 'x', '^', 'v')
# s: This controls the size of each marker


#### Bar Chart ####

# Vertical Bar Chart / Column chart

plt.bar(x,y,color='skyblue',width=5)     # Bar thickness → use width
plt.title('Bar chart')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()

# Horizontal Bar Chart

plt.barh(x,y,color='purple',height=5)      # height → thickness of bars
plt.title('Horizontal Bar chart')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()
