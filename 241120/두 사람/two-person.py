a, b = map(str, input().split())
c, d = map(str, input().split())

if (int(a) >= 19 or int(c) >= 19) and (b == "M" or d == "M"):
    print(1)
else:
    print(0)