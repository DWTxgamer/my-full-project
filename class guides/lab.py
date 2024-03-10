import random

ttime = []

x = 0
y = 0
z = 0
i = 0
r = 0
wt = 0

def time():
    t = wt/60
    t = t/60
    t = t/60
    if t >= 100:
        t = t/100
        t = t/60
        if t >= 60:
            t = t/100
            if t >= 60 and t <= 100:
                t = t/60
                t/100
    strtime = str(t)
    s = strtime[::-1]
    r = len(strtime)
    while r > 0:
        r -=1
        if strtime[r] == '.':
            tt = strtime[:r+3]
            return tt
        if r == -1:
            break

while True:
    x = random.randint(0,100)
    y = random.randint(0,100)
    z = random.randint(0,100)
    print(f'{x} // {y} // {z} ')
    i += 1
    wt += 100
    if x == y and y == z:
        print('')
        print(f'Simmilar numbers found in {i} attempts {x} // {y} // {z} in {time()} seconds ')
        break


    



