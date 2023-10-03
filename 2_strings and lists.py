string = input()
a, b, c, d = list(map(int, input().split()))
print(string[a:b+1], string[c:d+1])