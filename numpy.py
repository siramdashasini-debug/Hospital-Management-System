import numpy as np

marks = np.array([
    [85, 78, 92],
    [70, 88, 80],
    [90, 95, 94],
    [60, 65, 70],
    [76, 84, 81]
])

print("Marks:\n", marks)

total = np.sum(marks, axis=1)
average = np.mean(marks, axis=1)

print("\nTotal Marks")
print(total)

print("\nAverage Marks")
print(average)

top_student = np.argmax(total)

print("\nTop Student Index:", top_student)

subject_average = np.mean(marks, axis=0)

print("\nSubject-wise Average")
print(subject_average)