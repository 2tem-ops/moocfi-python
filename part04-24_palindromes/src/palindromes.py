def palindromes(word: str) -> bool:
    check1 = []
    check2 = []
    counter = 0
    for i in range(len(word) -1, -1, -1):
        check1.append(word[i])
    for i in word:
        check2.append(i)

    for letter in check1:
        if letter == check2[counter]:
            counter += 1
    
    if counter == len(check1):
        return True
    else:
        return False

while True:
    word = input("Please type in a palindrome: ")
    if palindromes(word):
        print(f"{word} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")


