def find_words(search_term: str) -> list:
    res = []
    words = []
    constraints = {}
    
    with open("words.txt") as file:
        for line in file:
            words.append(line.strip())
            
    if search_term.endswith("*"):
        for word in words:
            if word.startswith(search_term[0:-1]):
                res.append(word)
    elif search_term.startswith("*"):
        for word in words:
            if word.endswith(search_term[1:]):
                res.append(word)
                
    if "." in search_term:
        words = [i for i in words if len(i) == len(search_term)]
        for index, char in enumerate(search_term):
            if char != ".":
                constraints[index] = char
                
        res = [w for w in words if all(i < len(w) and w[i] == char for i, char in constraints.items())]
        
    if "." not in search_term and "*" not in search_term:
        for word in words:
            if word == search_term:
                res.append(word)
                
    
    return res

if __name__ == "__main__":
    #print(find_words("*vokes"))
    print(find_words(".a.e"))