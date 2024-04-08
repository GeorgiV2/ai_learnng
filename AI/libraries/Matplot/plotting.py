import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
categories = ['A', 'B', 'C', 'D', 'E']
values = [20, 35, 30, 25, 40]
ages = np.random.randint(18, 60, size=100)

# Creating a new figure and axis
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Plot 1: Line Plot
axs[0, 0].plot(x, y1, label='sin(x)', color='blue', linestyle='-', marker='o')
axs[0, 0].plot(x, y2, label='cos(x)', color='red', linestyle='--', marker='x')
axs[0, 0].set_title('Line Plot')
axs[0, 0].legend()

# Plot 2: Scatter Plot
axs[0, 1].scatter(x, y1, label='sin(x)', color='green', marker='o')
axs[0, 1].scatter(x, y2, label='cos(x)', color='orange', marker='x')
axs[0, 1].set_title('Scatter Plot')
axs[0, 1].legend()

# Plot 3: Bar Plot
axs[1, 0].bar(categories, values, color='purple')
axs[1, 0].set_title('Bar Plot')

# Plot 4: Histogram
axs[1, 1].hist(ages, bins=20, color='gray', edgecolor='black')
axs[1, 1].set_title('Histogram')

# Adjust layout
plt.tight_layout()

# Save the plot as a PNG file
plt.savefig('basic_plots.png')

# Display the plot
plt.show()
