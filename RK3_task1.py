import math

x = float(input())
y = float(input())
alpha = float(input())

x_total = x * math.cos(alpha) - y * math.sin(alpha)
y_total = x * math.sin(alpha) + y * math.cos(alpha)

print('x = ', x_total, '\ny = ', y_total)
