# What is Matplotlib?

# Matplotlib is a powerful Python library used for data visualization.
# It allows you to create static, animated, and interactive plots.
# Built on NumPy arrays — integrates easily with Pandas and SciPy.

import matplotlib.pyplot as plt

# pyplot provides a MATLAB-like interface for creating figures

# # Basic Plotting - Line Plot

a = [1,2,3,4,5]
b = [10,17,20,15,6]

plt.plot(a,b)    # plt.plot() plots a line graph of y vs x
plt.show()     # plt.show() displays the figure window


# Role of plt.show() in Matplotlib

# plt.show() is a Matplotlib function that displays the figure or chart you have created.

 
# What if You Don’t Use plt.show()?

# In Jupyter Notebook: Sometimes you still see the plot — because Jupyter automatically calls show() behind the scenes for the last line of code.
# Multiple Plots: Without plt.show(), you might get mixed or incomplete plots

# Multiple Plots Example - using .show()

# plot 1
plt.plot([1,2,3,4],[24,6,45,25])
plt.title('Figure 1')
plt.show()

# plot 2
plt.plot([1,2,3,4],[14,63,8,35])
plt.title('Figure 2')
plt.show()

# Multiple Plots Example - without using .show()

# plot 1
plt.plot([1,2,3],[3,2,1])
plt.title('Figure 1')

# plot 2
plt.plot([1,2,3],[1,2,3])
plt.title('Figure 2')

plt.show()


