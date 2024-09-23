import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
temperature = [5, 7, 10, 14, 18, 22, 25, 24, 20, 15, 10, 6]  # Temperature data
rainfall = [50, 40, 45, 60, 70, 80, 90, 100, 85, 60, 55, 50]  # Rainfall data

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.plot(months, temperature, marker='o', linestyle='-', color='b')
ax1.set_title('Monthly Temperature Data')
ax1.set_xlabel('Months')
ax1.set_ylabel('Temperature (°C)')
ax1.grid(True)

ax2.scatter(months, rainfall, color='g')
ax2.set_title('Monthly Rainfall Data')
ax2.set_xlabel('Months')
ax2.set_ylabel('Rainfall (mm)')
ax2.grid(True)

plt.tight_layout()

plt.show()
