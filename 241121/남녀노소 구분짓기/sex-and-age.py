# 변수 선언, 입력
gender = int(input())
age = int(input())

# gender가 1인지 2인지 판단하기
if gender == 0:
    # gender가 1일 때, age가 19보다 크다면 MAN이, 크지 않다면 BOY가 됩니다.
    if age >= 19:
        print("MAN")
    else:
    	print("BOY")
else:
    # gender가 2일 때, age가 19보다 크다면 WOMAN이, 크지 않다면 GIRL이 됩니다.
    if age >= 19:
        print("WOMAN")
    else:
        print("GIRL")