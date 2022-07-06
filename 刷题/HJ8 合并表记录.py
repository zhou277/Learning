n = int(input())
dic = {}
for i in range(0, n):
    index, value = map(int, input().split())
    if index in dic:
        dic[index] += value
    else:
        dic[index] = value
for name in sorted(dic.keys()):
    print(name, end=' ')
    print(dic[name])
