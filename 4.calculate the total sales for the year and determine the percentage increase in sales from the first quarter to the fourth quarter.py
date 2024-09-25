import numpy as np

np.random.seed(42)

sales_data = np.random.randint(100000, 500000, size=4)

print("Quarterly Sales Data:")
for quarter, sales in enumerate(sales_data, start=1):
    print(f"Q{quarter}: ${sales:,}")

total_sales = np.sum(sales_data)

percentage_increase = ((sales_data[3] - sales_data[0]) / sales_data[0]) * 100

print(f"\nTotal Sales for the Year: ${total_sales:,}")
print(f"Percentage Increase from Q1 to Q4: {percentage_increase:.2f}%")
