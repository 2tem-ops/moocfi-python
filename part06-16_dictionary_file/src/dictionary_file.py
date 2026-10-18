while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    function = int(input("Function: "))
    
    if function == 1:
        fin = input("The word in Finnish: ")
        eng = input("The word in English: ")
        with open("dictionary.txt", "a") as file:
            file.write(f"{fin};{eng}\n")
            
        print("Dictionary entry added")
        
    elif function == 2:
        search_term = input("Search term: ")
        with open("dictionary.txt") as file:
            for line in file:
                line = line.strip().split(";")
                for w in line:
                    if search_term in w:
                        print(f"{line[0]} - {line[1]}")
        
    elif function == 3:
        print("Bye!")
        break
    