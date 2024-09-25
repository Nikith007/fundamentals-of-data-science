import pandas as pd
import numpy as np
import scipy.stats as stats
file_path = "D:/Slot-D/fods/code/Q22sample.csv" 
data = pd.read_csv(file_path)
ratings = data['rating'] 
def confidence_interval(data, confidence=0.95):
    mean = np.mean(data)
    std_err = stats.sem(data)
    h = std_err * stats.t.ppf((1 + confidence) / 2, len(data) - 1)
    return mean - h, mean + h
ci = confidence_interval(ratings)
print(f"Confidence Interval for the average rating: {ci}")
