temp = input()
while len(temp)>0:
    print(temp[:8].ljust(8,"0"))
    temp = temp[8:]
