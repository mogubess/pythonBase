
x=100
y=20
z=[1,2,3]
if x == 100 and x > 40 and x < 200:
    print("OK1")
else:
    print("NG1")

if x == 100 and x > 40 and x < 50:
    print("NG2")
else:
    print("OK2")

if x == 100 and 1 in z and y < 50:
    print("OK3")
else:
    print("NG3")

if x == 100 and 1 not in z and y < 50:
    print("NG4")
else:
    print("OK4")

if x == 101 or 3 not in z or y < 50:
    print("OK5")
else:
    print("NG5")
