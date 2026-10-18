def add_student(database: dict, name: str):
    database[name] = ()

def add_course(database: dict, name: str, course: tuple):
    try:
        student_courses = list(database[name])
        
        if 0 not in course:
            for i, existing_course in enumerate(student_courses):
                if existing_course[0] == course[0]:
                    if existing_course[1] < course[1]:
                        updated_course = (existing_course[0], course[1])
                        student_courses[i] = updated_course
                    
                    database[name] = tuple(student_courses)
                    return
                
            database[name] = tuple(student_courses + [course])
            
    except KeyError:
        print("invalid student or database")

def print_student(database: dict, name: str):
    total_grade = 0
    student = database.get(name)
    if name not in database:
        print(f"{name}: no such person in the database")
    else:
        print(f"{name}:")
    
    if student and name in database:
        print(f" {len(student)} completed courses:")
        for course, grade in student:
            print(f"  {course} {grade}")
            total_grade += grade
        print(f" average grade {total_grade / len(student)}")
    else:
        if name in database:
            print(" no completed courses")
        
def summary(database: dict):
    average = 0
    avgs = []
    names = []
    courses = []
    
    for name in database:
        student = database[name]
        for i in student:
            average += i[-1]
            #print(f"grade: {i[-1]} courses: {len(student)} name: {name}")
        courses.append(len(student))
        if len(student) != 0:
            avgs.append(average / len(student))
        else:
            avgs.append(0)
        names.append(name)
        average = 0
    #print(avgs, names, courses)
    
    print(f"students {len(database)}")
    print(f"most courses completed {max(courses)} {names[courses.index(max(courses))]}")
    print(f"best average grade {max(avgs)} {names[avgs.index(max(avgs))]}")
            

if __name__ == "__main__":
    students = {}
    add_student(students, "Jack")
    add_student(students, "Mary")
    add_student(students, "Andy")
    add_course(students, "Jack", ("payton", 3))
    add_course(students, "Jack", ("payton", 4))
    add_course(students, "Mary", ("java", 3))
    add_course(students, "Mary", ("lua", 3))
    add_course(students, "Mary", ("c++", 3))
    add_course(students, "Jack", ("rust", 5))
    print_student(students, "Jack")
    print_student(students, "Amy")
    print_student(students, "Andy")
    summary(students)