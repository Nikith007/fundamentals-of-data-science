import pandas as pd

data = {
    'product_name': ['Laptop', 'Phone', 'Laptop', 'Tablet', 'Headphones', 'Phone', 'Tablet', 'Headphones', 'Phone', 'Laptop'],
    'quantity_sold': [2, 5, 3, 4, 2, 6, 1, 3, 4, 1]
}

sales_data = pd.DataFrame(data)

total_quantity_sold = sales_data.groupby('product_name')['quantity_sold'].sum()

top_products = total_quantity_sold.sort_values(ascending=False)

top_5_products = top_products.head(5)

print("Top 5 products sold the most in the past month:")
print(top_5_products)
