import numpy as np

np.random.seed(42)

num_models = 10
fuel_efficiency = np.random.uniform(20, 40, num_models)

print("Fuel Efficiency Data (miles per gallon):")
for i, efficiency in enumerate(fuel_efficiency, 1):
    print(f"Model {i}: {efficiency:.2f} mpg")

average_efficiency = np.mean(fuel_efficiency)

model1_index = 0
model2_index = -1
model1_efficiency = fuel_efficiency[model1_index]
model2_efficiency = fuel_efficiency[model2_index]

percentage_improvement = ((model2_efficiency - model1_efficiency) / model1_efficiency) * 100

print(f"\nAverage Fuel Efficiency: {average_efficiency:.2f} mpg")
print(f"Model 1 Efficiency: {model1_efficiency:.2f} mpg")
print(f"Model 2 Efficiency: {model2_efficiency:.2f} mpg")
print(f"Percentage Improvement: {percentage_improvement:.2f}%")
