import random

a = input("請出 剪刀 布 石頭")

com = random.randint(0, 2)

trans = "剪刀","布","石頭"

print("你出的拳",a)
print("電腦出的拳",trans[com])

if trans[com] == a:
    print("平手")

elif a == abs(com - 1) % 3:
    print("你贏了")
else:
    print("我輸了")

