def f1(n, k):
    if n == 1:
        return 'В'
    l = (1 << (n - 1)) - 1
    if k < l:
        return f1(n - 1, k)
    elif k == l:
        return 'Т'
    else:
        m = (1 << n) - 2 - k
        t = {'В': 'Д', 'Д': 'К', 'К': 'Т', 'Т': 'В'}
        return t[f1(n - 1, m)]
n, k = map(int, input().split())
print(f1(n, k))