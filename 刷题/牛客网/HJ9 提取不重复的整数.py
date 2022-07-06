a = input()
a = a[::-1]
num = ""
for i in range(0, len(a)):
    if a[i] not in num:
        num += (a[i])
    else:
        continue
    i += 1

print(num)
