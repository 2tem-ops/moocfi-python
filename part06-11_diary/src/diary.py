def main():
    while True:
        print("1 - add an entry, 2 - read entries, 0 - quit")
        try:
            function = int(input("Function: "))
            if function == 0:
                print("Bye now!")
                break
            elif function == 1:
                with open("diary.txt", "a") as diary:
                    diary.write(input("Diary entry: ") + "\n")
                    print("Diary saved\n")   
            elif function == 2:
                with open("diary.txt") as diary:
                    print("Entries:")
                    for line in diary:
                        print(line.strip())   
        except ValueError as e:
            print(f"Invalid function: {e}")
            break
              
main()