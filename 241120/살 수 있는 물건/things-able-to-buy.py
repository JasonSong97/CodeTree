a = int(input())

money = [("book", 3000), ("mask", 1000)]

for m in money:
    if a < 1000:
        print("no")
        break
    if (a // m[1]) >= 1:
        print(m[0])
        break
