import pandas as pd
data = pd.read_csv("D:/Slot-D/fods/code/Q36sample.csv")
mean_price = data['Closing Price'].mean()
std_price = data['Closing Price'].std()
print(f'Mean Closing Price: ${mean_price:.2f}')
print(f'Standard Deviation of Closing Price: ${std_price:.2f}')
