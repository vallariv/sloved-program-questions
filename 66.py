student_scores = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
highest_score_student = max(student_scores, key=lambda x: x[1])
print("Student with the highest score:", highest_score_student[0])
