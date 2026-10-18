def older_people(people: list, year: int) -> list[str]:
    names = [element for tupl in people for element in tupl if type(element) is str]
    dob = [element for tupl in people for element in tupl if type(element) is int]
    return [names[dob.index(i)] for i in dob if i < year]

if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    older = older_people(people, 1979)
    print(older)