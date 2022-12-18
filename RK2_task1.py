x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
xa = int(input())
ya = int(input())
xb = int(input())
yb = int(input())
a_bin = ''
b_bin = ''
total_bin = ''

if xa < x1:
    if ya < y1:
        a_bin = '1001'
    elif ya > y2:
        a_bin = '1010'
    else:
        a_bin = '1000'
elif xa > x2:
    if ya < y1:
        a_bin = '0101'
    elif ya > y2:
        a_bin = '0110'
    else:
        a_bin = '0100'
elif x1 <= xa <= x2:
    if ya < y1:
        a_bin = '0001'
    elif ya > y2:
        a_bin = '0010'
    else:
        a_bin = '0000'

if xb < x1:
    if yb < y1:
        b_bin = '1001'
    elif yb > y2:
        b_bin = '1010'
    else:
        b_bin = '1000'
elif xb > x2:
    if yb < y1:
        b_bin = '0101'
    elif yb > y2:
        b_bin = '0110'
    else:
        b_bin = '0100'
elif x1 <= xb <= x2:
    if yb < y1:
        b_bin = '0001'
    elif yb > y2:
        b_bin = '0010'
    else:
        b_bin = '0000'

for i in range(len(a_bin)):
    if a_bin[i] == b_bin[i]:
        total_bin += '1'
    else:
        total_bin += '0'

if total_bin == '0000':
    print('пересечение')
else:
    print('нет пересечения')
