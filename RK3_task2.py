xa = int(input())
ya = int(input())
za = int(input())
xb = int(input())
yb = int(input())
zb = int(input())
xc = int(input())
yc = int(input())
zc = int(input())

x1 = (yb - ya) * (zc - za)
x2 = (zb - za) * (yc - ya)
y1 = (xb - xa) * (zc - za)
y2 = (zb - za) * (xc - xa)
z1 = (xb - xa) * (yc - ya)
z2 = (yb - ya) * (xc - xa)

x_normal_vector = x1 - x2
y_normal_vector = - y1 + y2
z_normal_vector = z1 - z2

print('(' + str(x_normal_vector) + ',' + str(y_normal_vector) + ',' + str(z_normal_vector) + ')')