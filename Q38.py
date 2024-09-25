import pandas as pd
data = pd.read_csv("D:/Slot-D/fods/code/Q38sample.csv")
mean_temp_per_city = data.groupby('City')['Temperature'].mean()
print(mean_temp_per_city)
