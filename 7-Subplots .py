import matplotlib.pyplot as plt
import numpy as np

#### Subplots (Multiple Plots in One Figure) ####

# What is a Subplot?

# A subplot is a plot inside a figure.
# You can have multiple plots arranged in rows and columns within the same figure.
# Useful for visualizing multiple datasets side by side.

# **`Using plt.subplot()`**

# **Syntax:** plt.subplot(nrows, ncols, plot_number)

# | Parameter     | Description                                                            |
# | ------------- | ---------------------------------------------------------------------- |
# | `nrows`       | Number of rows of subplots                                             |
# | `ncols`       | Number of columns of subplots                                          |
# | `plot_number` | Position of current plot (1-based index, left to right, top to bottom) |

year = [2020,2021,2022,2023,2024,2025,2026]
sales = np.random.randint(100000,1000000,size=7)

plt.figure(figsize=(10,8))    # plt.figure(figsize=(width, height)) → Set the overall figure size

plt.subplot(2,2,1)        # plt.subplot() → Specify row, column, and plot index
plt.plot(year,sales)
plt.title('Line chart')

plt.subplot(2,2,2)
plt.scatter(year,sales)
plt.title('Scatter Chart')

plt.subplot(2,2,3)
plt.bar(year,sales)
plt.title('Bar cahrt')

plt.subplot(2,2,4)
plt.pie(sales,labels=year)
plt.title('Pie Chart')

plt.tight_layout()      # plt.tight_layout() → Automatically adjusts spacing between subplots to avoid overlap
plt.show()


# Using plt.subplots()

# Syntax: fig, axes = plt.subplots(nrows, ncols, figsize=(width, height))

# fig → the overall figure
# axes → array of subplot axes objects

x = np.linspace(10,100,1000)
y1 = np.sin(x)
y2 = np.cos(x)
y3= x**2
y4 = np.sqrt(x)

fig, axes = plt.subplots(2, 2, figsize=(10, 8))  # 2x2 grid

axes[0, 0].plot(x, y1, color='blue')
axes[0, 0].set_title("Sine Wave")

axes[0, 1].plot(x, y2, color='red')
axes[0, 1].set_title("Cosine Wave")

axes[1, 0].plot(x, y3, color='green')
axes[1, 0].set_title("x Squared")

axes[1, 1].plot(x, y4, color='orange')
axes[1, 1].set_title("Square Root of x")

plt.tight_layout()
plt.show()