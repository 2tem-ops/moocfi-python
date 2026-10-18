from math import floor
import urllib.request, json


def retrieve_all() -> list:
    info = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    data = json.load(info)
        
    res = []
    
    for course in data:
        if course["enabled"] == True:
            res.append((course["fullName"], course["name"], course["year"], sum(course["exercises"])))
            
    return res

def retrieve_course(course_name: str):
    info = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
    data = json.load(info)
    result = {}
    
    max_students = 0
    total_hours = 0
    total_exercises = 0
        
    for stats in data.values():
        if stats["students"] > max_students:
            max_students = stats["students"]
        total_hours += stats["hour_total"]
        total_exercises += stats["exercise_total"]
        
    result["weeks"] = len(data)
    result["students"] = max_students
    result["hours"] = total_hours
    result["hours_average"] = floor(total_hours / max_students)
    result["exercises"] = total_exercises
    result["exercises_average"] = floor(total_exercises / max_students)

    return result

if __name__ == "__main__":
    retrieve_all()
    print(retrieve_course("docker2019"))