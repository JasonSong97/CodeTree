data = list(map(int, input().split()))



if data[0] == min(data):
    print(1, end = " ")
else:
    print(0, end = " ")
if data[0] == data[1] == data[2]:
    print(1)
else:
    print(0)