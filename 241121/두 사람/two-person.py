a, b = map(str, input().split())
c, d = map(str, input().split())

if (int(a) >= 19 and d == "M") and (b == "M" and int(c) >= 19):
    print(1)
else:
    print(0)