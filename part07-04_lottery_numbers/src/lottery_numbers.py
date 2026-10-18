from random import randint

def lottery_numbers(amount: int, lower: int, upper: int) -> list[int]:
    draw = []
    while len(draw) < amount:
        rnd = randint(lower, upper)
        if rnd not in draw:
            draw.append(rnd)
            
    return sorted(draw)
        
if __name__ == "__main__":
    lottery_numbers(1, 1, 10)