from datetime import datetime, timedelta

# if False:
filename = input("Filename: ")
start = input("Starting date: ")
days = int(input("How many days: "))
print("Please type in screen time in minutes on each day (TV computer mobile):")
# else:
#     filename = "late_june.txt"
#     start = "14.12.2020"
#     days = 5

count = datetime.strptime(start, "%d.%m.%Y")

count2 = count
start = count.strftime("%d.%m.%Y")
end = (count + timedelta(days=days - 1)).strftime("%d.%m.%Y")

print("Please type in screen time in minutes on each day (TV computer mobile):")

times = []
amount = 0

for _ in range(days):
    screentime = input(f"Screen time {count.strftime("%d.%m.%Y")}: ")
    times.append(screentime.split())
    amount += 1
    count += timedelta(days=1)
    
total_mins = [int(j) for i in times for j in i]
    
with open(filename, "w") as file:
    file.write(f"Time period: {start}-{end}\n")
    file.write(f"Total minutes: {sum(total_mins)}\n")
    file.write(f"Average minutes: {sum(total_mins) / amount}\n")
    
    for time in times: 
        file.write(f"{count2.strftime("%d.%m.%Y")}: {"/".join(time)}\n")
        count2 += timedelta(days=1)
        
print(f"Date stored in file {filename}")