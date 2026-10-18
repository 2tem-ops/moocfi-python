def oldest_person(people: list) -> str:
    names = [element for tpl in people for element in tpl if type(element) is str]
    dob = [element for tpl in people for element in tpl if type(element) is int]
    
    return names[dob.index(min(dob))]
            


if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    print(oldest_person(people))