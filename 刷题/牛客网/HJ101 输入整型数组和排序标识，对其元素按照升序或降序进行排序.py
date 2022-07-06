k = int(input())
num = list(map(int, input().split()))
flag = input()
if flag == '0':
    num = sorted(num)
else:
    num = sorted(num, reverse=True)
for i in num:
    print(i, end=' ')
