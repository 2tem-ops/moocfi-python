def create_tuple(x: int, y: int, z: int) -> tuple[int, int, int]:
    res = (min(x, y, z), max(x, y, z), x + y + z)
    return res

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))