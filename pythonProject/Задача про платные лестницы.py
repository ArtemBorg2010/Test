n = int(input())
c = [int(i) for i in input().split()]
e = 0
while len(c) != n:
    print('Кол-во элементов должно быть равно верхнему числу!')
    c = [int(i) for i in input().split()]
t = -1

while t != len(c) - 1:
    if t == len(c) - 2:
        t = t + 1
    elif t == len(c) - 3:
        t = t + 2
    elif c[t + 1] > c[t + 2]:
        t = t + 2
    elif c[t + 1] <= c[t + 2]:
        t = t + 1
    e = e + c[t]
print(e)
