import matplotlib.pyplot as plt

days = list(range(1, 31))  # Days in a month
sales = [200, 210, 215, 220, 250, 260, 240, 230, 220, 270, 
         280, 290, 300, 310, 320, 310, 300, 295, 290, 285,
         280, 275, 270, 265, 260, 255, 250, 245, 240, 235]  # Sales data

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 12))

ax1.plot(days, sales, marker='o', linestyle='-', color='b')
ax1.set_title('Product Sales Over a Month - Line Plot')
ax1.set_xlabel('Days of the Month')
ax1.set_ylabel('Sales')
ax1.grid(True)

ax2.scatter(days, sales, color='r')
ax2.set_title('Product Sales Over a Month - Scatter Plot')
ax2.set_xlabel('Days of the Month')
ax2.set_ylabel('Sales')
ax2.grid(True)

ax3.bar(days, sales, color='g')
ax3.set_title('Product Sales Over a Month - Bar Plot')
ax3.set_xlabel('Days of the Month')
ax3.set_ylabel('Sales')
ax3.grid(axis='y')

plt.tight_layout()

plt.show()
