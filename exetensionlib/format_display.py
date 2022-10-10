
t = (1,2,3)
print('{t[0]}'.format(t=t))
print('{0[2]}'.format(t))

print('{0} {2}'.format(*t))

d = {'name':'jun', 'family':'sakai'}
print('{0[name]} {0[family]}'.format(d))

print('{name} {family}'.format(**d))


#出力の左寄せ、右寄せ、中央よせを数字で指定できる
print('{:<30}'.format('left'))
print('{:>30}'.format('right'))
print('{:^30}'.format('center'))

print('{0:^30}'.format('center'))
# ************center************　スペースの代わりにアスタリスクで
print('{0:*^30}'.format('center'))
print('{name:{fill}{align}{width}}'.format(name='center', fill='*', align='^',width=30))

# お金の表示などに使える(123,456,789)
print('{:,}'.format(123456789))

# float? fを付けるとある程度小数点以下まで表示する
# +3.140000 -3.140000
# +3.14 -3.14
print('{:+f} {:+f}'.format(3.14,-3.14))
print('{:+} {:+}'.format(3.14,-3.14))

# 86.36%
print('{:.2%}'.format(19/22))
# 0.8636363636363636
print('{}'.format(19/22))

# 100 0x64 0o144 0b1100100
print(int(100),hex(100),oct(100),bin(100))
# 100 0x64 0o144 0b1100100
print('{0:d} {0:#x} {0:#o} {0:#b}'.format(100))
# 100 64 144 1100100
print('{0:d} {0:x} {0:o} {0:b}'.format(100))

for i in range(20):
    for base in 'bdX':
        print('{:5{base}}'.format(i, base=base),end=' ')
    print()
# output --------------------
#     0     0     0 
#     1     1     1 
#    10     2     2
#    11     3     3
#   100     4     4
#   101     5     5
#   110     6     6
#   111     7     7
#  1000     8     8
#  1001     9     9
#  1010    10     A
#  1011    11     B
#  1100    12     C
#  1101    13     D
#  1110    14     E
#  1111    15     F
# 10000    16    10
# 10001    17    11
# 10010    18    12
# 10011    19    13