def new_person(name: str, age: int) -> tuple:
    if not name or len(name.split()) < 2 or len(name) > 40:
        raise ValueError
    if age < 0 or age > 150:
        raise ValueError
    
    return name, age

if __name__ == "__main__":
    print(new_person("hi", 149))