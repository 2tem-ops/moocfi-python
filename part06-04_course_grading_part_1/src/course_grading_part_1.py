student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")

ids = {}

with open(exercise_data) as file:
    for line in file:
        line = line.replace("\n", "")
        parts = line.split(";")
        id = parts[0]
        grades = [int(num) for num in parts[1:] if "e" not in num]
        if id == "id":
            continue
        ids[id] = sum(grades)
        
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
        
for id, grade in ids.items():
    if id in students:
        student = students[id]
        print(student, grade)