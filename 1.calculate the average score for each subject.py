import numpy as np

np.random.seed(42)  
student_scores = np.random.randint(60, 100, size=(32, 4))

subject_averages = np.mean(student_scores, axis=0)

subjects = ['Math', 'Science', 'English', 'History']
highest_avg_index = np.argmax(subject_averages)
highest_avg_subject = subjects[highest_avg_index]

print("Average scores for each subject:")
for subject, avg_score in zip(subjects, subject_averages):
    print(f"{subject}: {avg_score:.2f}")

print(f"\nThe subject with the highest average score is {highest_avg_subject} with an average of {subject_averages[highest_avg_index]:.2f}")
