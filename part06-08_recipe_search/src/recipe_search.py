## 1
            
def search_by_name(filename: str, word: str) -> list:
    res = []
    
    if filename == "recipes1.txt":
        for recipe in recipes1:
            for el in recipe:
                if word.capitalize() in el or word.lower() in el:
                    res.append(el)
        return res
    
    elif filename == "recipes2.txt":
        for recipe in recipes2:
            for el in recipe:
                if word.capitalize() in el or word.lower() in el:
                    res.append(el)
        return res
    
    else:
        return []
    
def search_by_time(filename: str, prep_time: int) -> list:
    res = []
    
    if filename == "recipes1.txt":
        for recipe in recipes1:
            for el in recipe:
                if el.isdigit():
                    if int(el) <= prep_time:
                        res.append(recipe[0] + "," + " " + f"preparation time {el} min")
        return res
    
    elif filename == "recipes2.txt":
        for recipe in recipes2:
            for el in recipe:
                if el.isdigit():
                    if int(el) <= prep_time:
                        res.append(recipe[0] + "," + " " + f"preparation time {el} min")
        return res
    
    else:
        return []
    
            
            
            
if __name__ == "__main__":
    lst1 = []
    lst2 = []

    current1 = []
    recipes1 = []

    current2 = []
    recipes2 = []
    
    with open("recipes1.txt") as file:
        for line in file:
            lst1.append(line.strip())
            
    for line in lst1:
        if line == "":
            if current1:
                recipes1.append(current1)
                current1 = []
        else:
            current1.append(line)

    if current1:
        recipes1.append(current1)

    ## 2
    with open("recipes2.txt") as file:
        for line in file:
            lst2.append(line.strip())
            
    for line in lst2:
        if line == "":
            if current2:
                recipes2.append(current2)
                current2 = []
        else:
            current2.append(line)

    if current2:
        recipes2.append(current2)
    
    print(search_by_name("recipes1.txt", "cake"))
    for i in search_by_time("recipes1.txt", 20):
        print(i)