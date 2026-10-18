import json

def print_persons(filename: str):
    with open(filename) as file:
        data = file.read()
    information = json.loads(data)
    for info in information:
        print(info["name"], info["age"], "years", "(" + ", ".join([i for i in info["hobbies"]]) + ")")

if __name__ == "__main__":
    print_persons("file1.json")