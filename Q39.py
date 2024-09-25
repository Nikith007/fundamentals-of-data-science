import pandas as pd
data = pd.read_csv("D:/Slot-D/fods/code/Q39sample.csv")
total_sales_per_product = data.groupby('Product')['Sales ($)'].sum()
top_5_products = total_sales_per_product.nlargest(5)
print('Top 5 best-selling products:')
print(top_5_products)
