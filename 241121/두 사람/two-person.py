# 첫 번째 사람의 정보 입력받기
age1, gender1 = input().split()
age1 = int(age1)

# 두 번째 사람의 정보 입력받기
age2, gender2 = input().split()
age2 = int(age2)

# 조건 확인: 한 사람이라도 19세 이상이면서 남자인 경우
if (age1 >= 19 and gender1 == 'M') or (age2 >= 19 and gender2 == 'M'):
    print(1)
else:
    print(0)
