def get_neighbours(nums: list) -> list:
    return list(zip(nums[0::2], nums[1::2]))

def extract_exam_points(data: list) -> list:
    result = []
    
    for i in data:
        points = int(i[0])
        result.append(points)
        
    return result

def convert_into_exercise_points(data: list) -> list:
    exercise_points = 0
    result = []
    
    for i in data:
        exercises = int(i[1])
        exercise_points = exercises // 10
        result.append(exercise_points)
        
    return result

def find_total(exam_pts: list, exer_pts: list) -> list:
    result = []
    index = 0
    
    for i in exam_pts:
        total = i + exer_pts[index]
        result.append(total)
        index += 1
        
    return result

def total_average(total: list) -> str:
    operation = sum(total) / len(total)
    result = f"{operation:.1f}"
    
    return result

def convert_into_grade(total: list, ex_pts: list) -> list:
    result = []
    index = 0
    
    for i in total:
        if ex_pts[index] < 10:
            result.append(0)
        else:
            if 28 <= i <= 30:
                result.append(5)
            elif 24 <= i <= 27:
                result.append(4)
            elif 21 <= i <= 23:
                result.append(3)
            elif 18 <= i <= 20:
                result.append(2)            
            elif 15 <= i <= 17:
                result.append(1)
            else:
                result.append(0)
        index += 1
            
    return result  

def passing_percentage(grades: list) -> str:
    passers = 0
    total = len(grades)
    
    for i in grades:
        if i > 0:
            passers += 1
            
    operation = (passers / total) * 100       
    result = f"{operation:.1f}"
    
    return result
    

def main():
    data = []
    
    while True:
        entry = input("Exam points and exercises completed: ") # points | exercises
        
        if not entry:
            break
        
        data += entry.split()

    # split data into pairs of (points | exercises)
    result = get_neighbours(data)
    
    # get what we actually need
    exercise_points = convert_into_exercise_points(result)
    exam_points = extract_exam_points(result)
    
    # find the total points student got
    total = find_total(exam_points, exercise_points)
    
    # convert total points -> grade, fail those who have < 10 exam points
    grades = convert_into_grade(total, exam_points)
    
    # get grade distribution
    fail, one, two, three, four, five = 0, 0, 0, 0, 0, 0
    
    for i in grades:
        if i == 0:
            fail += 1
        elif i == 1:
            one += 1
        elif i == 2:
            two += 1
        elif i == 3:
            three += 1
        elif i == 4:
            four += 1
        elif i == 5:
            five += 1
    
    """
    # debug
    
    print(f"Exercise points: {exercise_points}")
    print(f"Exam points: {exam_points}")
    print(f"Total points: {total}")
    print(f"Grades: {grades}")
    """
    
    # final output
    print("Statistics:")
    print(f"Points average: {total_average(total)}", f"Pass percentage: {passing_percentage(grades)}", sep="\n")
    print("Grade distribution:")
            
    print(f"  5: {"*" * five}", f"  4: {"*" * four}", f"  3: {"*" * three}", f"  2: {"*" * two}", f"  1: {"*" * one}", f"  0: {"*" * fail}", sep="\n")
              
main()
