import numpy as np

np.random.seed(42)

num_houses = 100
house_data = np.zeros((num_houses, 3))

house_data[:, 0] = np.random.randint(2, 7, num_houses)  
house_data[:, 1] = np.random.randint(1000, 3000, num_houses)  
house_data[:, 2] = np.random.randint(200000, 800000, num_houses)  

print("Sample of house data:")
print(house_data[:5])

more_than_four_bedrooms = house_data[:, 0] > 4
filtered_houses = house_data[more_than_four_bedrooms]

average_price = np.mean(filtered_houses[:, 2])

print(f"\nNumber of houses with more than 4 bedrooms: {filtered_houses.shape[0]}")
print(f"Average sale price of houses with more than 4 bedrooms: ${average_price:.2f}")
