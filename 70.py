students = [
    {'name': 'Alice', 'score': 85},
    {'name': 'Bob', 'score': 92},
    {'name': 'Charlie', 'score': 78}
]
sorted_students = sorted(students, key=lambda x: x['score'], reverse=True)
print("Students sorted by score in descending order:")
print(sorted_students)
