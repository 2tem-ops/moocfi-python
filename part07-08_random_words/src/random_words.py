from random import choice

def words(n: int, beginning: str) -> list:
    lst = []
    needed = []
    res = []
    
    with open("words.txt") as file:
        for line in file:
            lst.append(line.strip())
    
        for word in lst:
            if word.startswith(beginning):
                needed.append(word)
                
        if not needed or len(needed) < n:
            raise ValueError
                
        for _ in range(n):
            word = choice(needed)
            if word not in res:
                res.append(word)
            
    return res
            

if __name__ == "__main__":
    word_list = words(2, "ca")
    print(word_list)