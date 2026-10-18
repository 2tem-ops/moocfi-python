from fractions import Fraction

def fractionate(amount: int) -> list:
    res = []
    
    for _ in range(amount):
        res.append(Fraction(1, amount))
        
    return res

if __name__ == "__main__":
    print(fractionate(3))