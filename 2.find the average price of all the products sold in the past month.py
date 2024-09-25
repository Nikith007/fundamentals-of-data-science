import numpy as np

np.random.seed(42)

sales_data = np.random.randint(10, 100, size=(3, 3))

print("Sales Data:")
print(sales_data)

total_revenue = np.sum(sales_data)
total_items_sold = np.sum(sales_data[:, 1])

average_price = total_revenue / total_items_sold

print(f"\nTotal Revenue: ${total_revenue}")
print(f"Total Items Sold: {total_items_sold}")
print(f"Average Price: ${average_price:.2f}")
