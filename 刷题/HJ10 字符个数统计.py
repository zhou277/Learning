lista = []
string = input()
for i in range(0, len(string)):
    if string[i] not in lista:
        lista.append(string[i])
print(len(lista))

print(len(set(input().replace('\n', ''))))
