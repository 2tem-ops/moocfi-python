def filter_solutions():
    correct_lines = []
    incorrect_lines = []
    
    with open("solutions.csv") as file:
        for line in file:
            line = line.replace("\n", "").split(";")
            problem, solution = line[1], line[2]
            operator = problem[problem.find("+")]
            if operator != "+":
                operator = problem[problem.find("-")]
            if operator == "-":
                problem = problem.split("-")
                problem.append(operator)
                problem = [int(num) if num.isdigit() else num for num in problem]
                if int(problem[0]) - int(problem[1]) == int(solution):
                    with open("correct.csv", "a") as correct:
                        correct_lines.append(";".join(line))
                else:
                    with open("incorrect.csv", "a") as incorrect:
                        incorrect_lines.append(";".join(line))
            else:
                problem = problem.split("+")
                problem.append(operator)
                problem = [int(num) if num.isdigit() else num for num in problem]
                if int(problem[0]) + int(problem[1]) == int(solution):
                    with open("correct.csv") as correct:
                        correct_lines.append(";".join(line))
                else:
                    with open("incorrect.csv") as incorrect:
                        incorrect_lines.append(";".join(line))
                        
        with open("correct.csv", "w") as correct:
            correct.write("\n".join(correct_lines))

        with open("incorrect.csv", "w") as incorrect:
            incorrect.write("\n".join(incorrect_lines))
            
if __name__ == "__main__":   
    filter_solutions()