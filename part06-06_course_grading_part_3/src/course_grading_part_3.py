#if False:
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_points = input("Exam points: ")
"""
else:
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_points = "exam_points1.csv"
"""
    
exercises = {}

with open(exercise_data) as file:
    for line in file:
        line = line.replace("\n", "")
        parts = line.split(";")
        id = parts[0]
        grades = [int(num) for num in parts[1:] if "e" not in num]
        if id == "id":
            continue
        exercises[id] = sum(grades)
        
points = {}

with open(exam_points) as file:
    for line in file:
        line = line.replace("\n", "")
        parts = line.split(";")
        id = parts[0]
        exams = [int(num) for num in parts[1:] if "e" not in num]
        if id == "id":
            continue
        points[id] = sum(exams)
        
students = {}

with open(student_info) as file:
    for line in file:
        line = line.replace("\n", "")   
        parts = line.split(";")
        id = parts[0]
        name = parts[1] + " " + parts[2] 
        if id == "id":
            continue
        if name == "first" or name == "last":
            continue
        students[id] = name

grades = {}
exec_pts = {}

for id, exercise in exercises.items():
    if id in students and id in points and id in exercises:
        calc = exercise / 0.4
        grades[id] = min(int(calc // 10), 10)
        exec_pts[id] = min(int(calc // 10), 10)
        
for id, exam in points.items():
    if id in grades:
        grades[id] = grades[id] + exam
        
scores = {}

print(f"{"name":<29} {"exec_nbr":<9} {"exec_pts.":<9} {"exm_pts.":<9} {"tot_pts.":<9} {"grade":<9}")
            
for id, grade in grades.items():
    if id in students:
        student = students[id]
        score = 0
        if grade >= 28:
            score = 5
        elif 24 <= grade <= 27:
            score = 4
        elif 21 <= grade <= 23:
            score = 3
        elif 18 <= grade <= 20:
            score = 2
        elif 15 <= grade <= 17:
            score = 1
        else:
            score = 0
        scores[id] = score
        print(f"{student:<29} {exercises[id]:<9} {exec_pts[id]:<9} {points[id]:<9} {grades[id]:<9} {scores[id]:<9}")

"""
print(exercises)
print(exec_pts)
print(points)
print(grades)
print(scores)
"""