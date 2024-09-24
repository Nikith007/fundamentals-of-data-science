import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Step 1: Simulated clinical trial data
np.random.seed(42)
control_group = np.random.normal(100, 10, 30)  # placebo group
treatment_group = np.random.normal(110, 10, 30)  # treatment group

# Step 2: Perform hypothesis testing (independent t-test)
t_statistic, p_value = stats.ttest_ind(treatment_group, control_group)

# Step 3: Visualize the data using boxplots
plt.figure(figsize=(8, 5))
plt.boxplot([control_group, treatment_group], labels=['Control (Placebo)', 'Treatment (Drug)'])
plt.title(f'Control vs Treatment Group\nP-Value: {p_value:.5f}')
plt.ylabel('Effect Measure')

# Display the p-value
plt.axhline(np.mean(control_group), color='blue', linestyle='--', label='Control Mean')
plt.axhline(np.mean(treatment_group), color='red', linestyle='--', label='Treatment Mean')
plt.legend()

# Show plot
plt.show()

# Step 4: Output the results
print(f"T-Statistic: {t_statistic:.3f}")
print(f"P-Value: {p_value:.5f}")

# Interpret the p-value
if p_value < 0.05:
    print("The p-value is less than 0.05, rejecting the null hypothesis. The treatment has a statistically significant effect.")
else:
    print("The p-value is greater than 0.05, failing to reject the null hypothesis. The treatment does not have a statistically significant effect.")
