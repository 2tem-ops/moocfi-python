def filter_incorrect():
    weeks = []
    nums = []
    
    with open("lottery_numbers.csv") as file:
        for line in file:
            numbers = line[line.find(";") + 1:].strip().split(",")
            nums.append(numbers)
            
            week = line[5:line.find(";")].strip()
            weeks.append(week)
            
    print(nums)
    print(weeks)
        

if __name__ == "__main__":
    filter_incorrect()