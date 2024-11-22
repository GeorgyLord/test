def f(y):
    v = y[0]
    an = int(y[1:-1])
    e = y[-1]
    if v == 'N':
        if e == 'E':
            n = (an % 360)
        elif e == 'W':
            n = (360 - an) % 360
    elif v == 'S':
        if e == 'E':
            n = (180 + an) % 360
        elif e == 'W':
            n = (180 - an) % 360
    elif v == 'E':
        if e == 'N':
            n = (90 - an) % 360
        elif e == 'S':
            n = (90 + an) % 360
    elif v == 'W':
        if e == 'N':
            n = (270 + an) % 360
        elif e == 'S':
            n = (270 - an) % 360
    
    return n

K = int(input().strip())
a = input().strip().split()
m = {}
lp = {}
for index, y in enumerate(a):
    n = f(y)
    if n not in m:
        m[n] = 0
    m[n] += 1
    lp[n] = index + 1
mc = max(m.values())
ang = [an for an, count in m.items() if count == mc]
cang = min(ang)
res = lp[cang]
print(res)