k = int(input())
a = input().split()
last = 0
m = {} # угол, количество, индекс на последний элумент
ma = {'N': 0, 'E': 90, 'S': 180, 'W': 270}
dm = {
    ('N', 'E'): 1,
    ('N', 'W'): -1,
    ('S', 'W'): 1,
    ('S', 'E'): -1,
    ('E', 'S'): 1,
    ('E', 'N'): -1,
    ('W', 'N'): 1,
    ('W', 'S'): -1
}
for i in range(k):
    f = a[i][0]
    l = a[i][-1]
    mi = int(a[i][1:-1])
    ang = (ma[f] + dm[(f, l)] * mi)%360
    if ang not in m.keys():
        m[ang] = [1, i]
    else:
        m[ang] = [m[ang][0]+1, i]
m = list(m.items())
ind = 0
mm = 0
maxa = 0
ns = []
for i in range(len(m)):
    if m[i][1][0] > mm or (m[i][1][0] == mm and m[i][0] > maxa):
        mm = m[i][1][0]
        ind = m[i][1][1]
        maxa = m[i][0]
print(ind+1)

# for i in range(len(list(m.items()))):
# print(list(m.items()))
# print(list(m.items())[1][1][0])
# print(sorted(list(m.items()), key=lambda x: x[1][0]))
# ww=sorted(list(m.items()), key=lambda x: x[1][0])
# for i in range(len(ww)):
# 
#print(ind)
# print(sorted(m.items(), key=lambda i: i[0])[0][1][1]+1)