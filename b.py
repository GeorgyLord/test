def f(n, a):
    if all(a[i] >= a[i + 1] for i in range(n - 1)):
        return 0
    so = sorted(a, reverse=True)
    m = {value: i for i, value in enumerate(a)}
    w = [False] * n
    ti = 0
    for i in range(n):
        if w[i] or a[i] == so[i]:
            continue
        ss = 0
        x = i
        while not w[x]:
            w[x] = True
            x = m[so[x]]
            ss += 1
        if ss > 0:
            ti += ss + 1
    return ti
n = int(input())
a = list(map(int, input().split()))
print(f(n, a))