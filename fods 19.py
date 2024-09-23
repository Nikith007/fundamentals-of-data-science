import numpy as np
import scipy.stats as stats

drug_reduction = np.array([8, 9, 7, 10, 6, 12, 5, 11, 10, 9,
                           8, 7, 10, 9, 8, 6, 5, 7, 8, 10,
                           12, 11, 9, 8, 10])  

placebo_reduction = np.array([1, 2, 2, 1, 3, 2, 1, 2, 1, 3,
                              2, 3, 1, 2, 3, 2, 2, 1, 3, 2,
                              1, 2, 3, 1, 2]) 

def confidence_interval(data, confidence=0.95):
    n = len(data)
    mean = np.mean(data)
    std_dev = np.std(data, ddof=1)  
    z = stats.norm.ppf((1 + confidence) / 2)
    margin_of_error = z * (std_dev / np.sqrt(n))
    return mean - margin_of_error, mean + margin_of_error

drug_ci = confidence_interval(drug_reduction)
placebo_ci = confidence_interval(placebo_reduction)

print(f"95% Confidence Interval for Drug Group: {drug_ci}")
print(f"95% Confidence Interval for Placebo Group: {placebo_ci}")
