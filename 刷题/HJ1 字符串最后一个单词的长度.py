string = input()
i = -1
n = -len(string)
while i > n:
    i -= 1
    if string[i] == " ":
        i += 1
        break
print(-i)
