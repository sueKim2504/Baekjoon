# num: 1003
# title: 피보나치 함수
def fibonacci(n):
    a, b = 1, 0
    tmp = 0
    for _ in range(n):
        tmp = a + b
        a = b
        b = tmp
    return a, b

t = int(input())

for _ in range(t):
    n = int(input())
    for x in fibonacci(n):
        print(x, end = " ")
    print()
