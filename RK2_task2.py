xp1 = int(input())
yp1 = int(input())
xp2 = int(input())
yp2 = int(input())
xa = int(input())
ya = int(input())
xb = int(input())
yb = int(input())

nx = yp2 - yp1
ny = xp1 - xp2
ao = (xa - xp1)*nx + (ya - yp1)*ny
ab = (xb - xa)*nx + (yb - ya)*ny
t = - ao/ab
print(t)
