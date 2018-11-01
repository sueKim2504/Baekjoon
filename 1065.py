# num: 1065
# title: 한수
def han(n):
    if n < 100:
        return True
    else:
        l = list(str(n))
        if int(l[1]) - int(l[0]) != int(l[2]) - int(l[1]):
            return False
        return True

n = int(input())
cnt = 0
for number in range(1, n+1):
    if han(number) == True:
        cnt += 1

print(cnt)
