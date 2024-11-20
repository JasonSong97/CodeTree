import sys

input = sys.stdin.readline

n = int(input())
a, b, c, d = map(int, input().split())


print(1 if a > b else 0)
print(1 if a > c else 0)
print(1 if a > d else 0)
print(1 if a > e else 0)