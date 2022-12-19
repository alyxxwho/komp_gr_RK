xa = int(input())
ya = int(input())
za = int(input())
xb = int(input())
yb = int(input())
zb = int(input())
xc = int(input())
yc = int(input())
zc = int(input())
x = int(input())
y = int(input())

ab = (xa - x)*(yb - ya) - (xb - xa)*(ya - y)
bc = (xb - x)*(yc - yb) - (xc - xb)*(yb - y)
ac = (xc - x)*(ya - yc) - (xa - xc)*(yc - y)

if ab > 0 and bc > 0 and ac > 0 or ab < 0 and bc < 0 and ac < 0:
    print('Точка лежит внутри проекции')
else:
    print('Не лежит')
