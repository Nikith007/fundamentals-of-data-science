import numpy as np
import scipy.stats as stats


design_A = np.array([5.1, 5.6, 5.0, 5.3, 5.8, 5.7, 5.2, 5.4, 5.5, 5.9])

design_B = np.array([6.2, 6.5, 6.1, 6.3, 6.4, 6.0, 6.1, 6.5, 6.3, 6.2])

t_statistic, p_value = stats.ttest_ind(design_A, design_B)

print(f"T-statistic: {t_statistic:.4f}")
print(f"P-value: {p_value:.4f}")

alpha = 0.05  
if p_value < alpha:
    print("There is a statistically significant difference in conversion rates between design A and design B.")
else:
    print("There is no statistically significant difference in conversion rates between design A and design B.")
