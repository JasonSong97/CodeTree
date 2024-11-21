data = []
for _ in range(int(input())):
    temp = input().split()
    if temp[0] == "push_back":
        data.append(int(temp[1]))
    elif temp[0] == "get":
        print(data[int(temp[1]) - 1])
    elif temp[0] == "size":
        print(len(data))
    elif temp[0] == "pop_back":
        data.pop()