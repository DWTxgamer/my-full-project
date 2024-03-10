x = 0
j = 0
i = 0

while True:
    i += 1
    print(f'{j}:{x}.{i} ')
    if i == 900:
        i = 0
        x +=.1
    if x > 0.9:
        x += 1
    if x == 60:
        i = 0
        x = 0
        j += 1
    if j == 10:
        break