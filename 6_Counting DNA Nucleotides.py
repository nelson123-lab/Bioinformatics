string = input()
A, C, G, T = 0, 0, 0, 0
for i in string:
    if i == "A":
        A += 1
    elif i == "C":
        C += 1
    elif i == "G":
        G += 1
    elif i == "T":
        T += 1
    else: pass
print(A, C, G, T)
