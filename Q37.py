import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
data = pd.read_csv("D:/Slot-D/fods/code/Q37sample.csv")
correlation, _ = pearsonr(data['Study Time (hours)'], data['Exam Score'])
print(f'Correlation between study time and exam score: {correlation:.2f}')
plt.scatter(data['Study Time (hours)'], data['Exam Score'])
plt.xlabel('Study Time (hours)')
plt.ylabel('Exam Score')
plt.title('Study Time vs Exam Score')
plt.show()
