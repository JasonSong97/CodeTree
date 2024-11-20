n = int(input())

data = [("book", 3000), ("mask", 1000), ("pen", 500)]

for d in data:
    if n < 500:
        print("no")
        break
    if (n // d[1]) >= 1:
        print(d[0])
        break