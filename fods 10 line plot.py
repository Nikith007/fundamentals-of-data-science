import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
sales = [1500, 1800, 1700, 1600, 2100, 2300, 2200, 2000, 1900, 2400, 2500, 2600]

plt.figure(figsize=(10, 6))
plt.plot(months, sales, marker='o', color='b', linestyle='-', label='Sales')

plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Monthly Sales Data (Line Plot)')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()

plt.show()
