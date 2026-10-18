def longest(strings: list[str]) -> str:
    return max(strings, key=len)

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))