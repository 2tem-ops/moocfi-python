import string

layers = int(input("Layers: "))
square = layers + (layers + 2) // 2

alphabet = [""] + [i for i in string.ascii_uppercase]
res = []

for i in range(square):
    ltr = alphabet[layers]
    s = ltr * square
    res.append(s)
    print(s)
    left = s[0]
    right = s[-1]
    mid_slice = s[1:-1].replace(left, chr(ord(left) - 1))
    print(left + mid_slice + right)