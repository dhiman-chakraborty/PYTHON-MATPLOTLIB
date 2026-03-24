import matplotlib.pyplot as plt
import numpy as np

#### Pie Chart ####

category = ['iPhone','Vivo','Oppo','Xiome','Samsung','Motorola']
sales = [2568945,457796,6874122,9475322,1563789,5748952]
color = ['red','blue','yellow','pink','green','orange']

# pie chart 1

plt.pie(sales,labels=category)
plt.show()

# pie chart 2

plt.pie(sales,labels=category,colors=color,autopct='%1.2f%%',startangle=90)
plt.title('Mobile sales pie chart')
plt.axis('equal')     # Equal aspect ratio
plt.show()

# | Parameter    | Description                                                                                                       |
# | ------------ | ----------------------------------------------------------------------------------------------------------------- |
# |  values       | A list of numeric values representing the portion (e.g., [2568945,457796,6874122,9475322,1563789,5748952]).      |
# |  labels      | Names for each slice of the pie (['iPhone','Vivo','Oppo','Xiome','Samsung','Motorola']).                          |
# |  colors      | Colors for each slice (can be named colors, hex cods, or RGB values).                                             |
# |  autopct     | Used to **display percentages** on each slice.<br> '%1.1f%%' means show one decimal place (e.g., 45.0%).          |
# |  startangle  | Rotates the starting point of the pie chart (in degrees). Here 140° means the chart starts rotated 140 degrees.   |

# plt.axis('equal'): Ensures the pie chart is drawn as a circle rather than an ellipse. By default, Matplotlib might stretch the pie to fit 
# the figure window, so 'equal' keeps x and y axes the same scale.



#### Box Plot ####
# Shows spread and outliers of data.

# Box plot 1

data = np.random.randint(10,100,size=10)

plt.boxplot(data)
plt.title('Box plot')
plt.xlabel('x-axis')
plt.ylabel('Values')
plt.show()

# Box plot 2

data2 = np.random.randint(10,100,size=10)

plt.boxplot(
    data2,
    patch_artist=True,   # allows filling color
    boxprops=dict(facecolor='lightblue', color='blue', linewidth=2),
    whiskerprops=dict(color='green', linewidth=2),
    capprops=dict(color='red', linewidth=2),
    medianprops=dict(color='orange', linewidth=3)
)

plt.title('Decorated Box Plot', fontsize=14, color='purple')
plt.xlabel('Dataset', fontsize=12)
plt.ylabel('Values', fontsize=12)

plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()