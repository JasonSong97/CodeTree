a, b = map(str, input().split())
c = a if len(a) > len(b) else b

print(f"{c} {len(c)}")