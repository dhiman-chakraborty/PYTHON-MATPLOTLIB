import matplotlib.pyplot as plt

# Titles, labels, legend grid, Line Style, Color, Marker

x = [1,2,3,4,5]
y = [14,63,98,45,75]

# plt.plot(x, y, color='red', linestyle='--', marker='o')
# plt.plot(x, y, color='red', linestyle='--', marker='o', linewidth=2, markersize=10)
plt.plot(x,y,color='blue',linestyle=':',marker='.',linewidth=3,markersize=20)
plt.title('Customize Line Plot')
plt.xlabel('month')
plt.ylabel('sales')
plt.grid(True)    # plt.grid(False)
plt.show()

# Parameters explained
# | Property     | Example                       | Description       |
# | ------------ | ----------------------------- | ----------------- |
# | color        | 'r', 'blue', '#FF5733'        | Line color        |
# | linestyle    | '-', '--', ':', '-. '         | Line style        |
# | marker       | 'o', '^', 's', '*'            | Marker type       |
# | linewidth    | 2                             | Thickness of line |
# | markersize   | 8                             | Size of marker    |


plt.plot(x,y,color='g',linestyle='--',marker='o',linewidth=3,markersize=10)
plt.title('Sine wave')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid(False)
plt.show()

# Parameters explained
# color: line color ('r', 'b', 'g', hex codes)
# linestyle: '-', '--', ':', '-.', ''
# marker: 'o', 's', '*', '+', 'x'
# label: name for legend


### **Styling and Colors** ###

# Colors:
# * Names: `'red'`, `'green'`, `'blue'`
# * Short codes: `'r'`, `'g'`, `'b'`
# * Hex: `'#FF5733'`
# * RGB tuples: `(0.1, 0.2, 0.5)`

# Linestyles:
# * `'-'` solid
# * `'--'` dashed
# * `'-.'` dash-dot
# * `':'` dotted

# Markers:
# * `'o'` circle
# * `'s'` square
# * `'^'` triangle
# * `'*'` star

# Legend Position:
# - plt.legend(loc='upper right')   → top-right corner
# - plt.legend(loc='upper left')    → top-left corner
# - plt.legend(loc='lower right')   → bottom-right corner
# - plt.legend(loc='lower left')    → bottom-left corner
# - plt.legend(loc='center')        → center of figure
# - plt.legend(loc='best')          → automatically choose best position