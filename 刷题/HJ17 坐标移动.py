zuobiao = [0, 0]
zhiling = input().split(';')
print(zhiling)

for item in zhiling:
    try:
        direction = item[0]
        step = int(item[1:])
        if direction in ['A', 'S', 'W', 'D']:
            if step in range(0, 100):
                if direction == 'A':
                    zuobiao[0] -= step
                elif direction == 'S':
                    zuobiao[1] -= step
                elif direction == 'W':
                    zuobiao[1] += step
                elif direction == 'D':
                    zuobiao[0] += step
    except:
        continue

print(str(zuobiao[0]) + ',' + str(zuobiao[1]))
