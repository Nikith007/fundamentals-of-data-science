import pandas as pd

data = {
    'customer_id': [1, 2, 1, 3, 2, 3, 1],
    'order_date': ['2023-01-01', '2023-01-03', '2023-01-02', '2023-01-05', '2023-01-07', '2023-01-06', '2023-01-08'],
    'product_name': ['Product A', 'Product B', 'Product A', 'Product C', 'Product B', 'Product C', 'Product A'],
    'order_quantity': [2, 1, 3, 5, 4, 2, 1]
}

order_data = pd.DataFrame(data)

order_data['order_date'] = pd.to_datetime(order_data['order_date'])

total_orders_per_customer = order_data.groupby('customer_id')['product_name'].count()

average_order_quantity_per_product = order_data.groupby('product_name')['order_quantity'].mean()

earliest_order_date = order_data['order_date'].min()
latest_order_date = order_data['order_date'].max()

print("Total number of orders made by each customer:")
print(total_orders_per_customer)

print("\nAverage order quantity for each product:")
print(average_order_quantity_per_product)

print("\nEarliest order date:", earliest_order_date)
print("Latest order date:", latest_order_date)
