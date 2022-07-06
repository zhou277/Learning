num = int(input())
ming = []
for i in range(0, num):
    ming.append(int(input()))
ming.sort()
lista = []
while ming:
    e = ming.pop(0)
    if e not in lista:
        lista.append(e)
    else:
        continue
for i in range(0, len(lista)):
    print(lista[i])
