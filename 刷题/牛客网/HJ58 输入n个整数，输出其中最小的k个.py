n, k = map(int, input().split())
num = list(map(int, input().split()))
num = sorted(num)
for i in num[:k]:
    print(i, end=' ')
