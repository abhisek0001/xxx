#testing account
#----------------------------------simple calculatro code in python-----------------------------------------
# you can change this ver to customize the code
from re import X
from turtle import st


print("1️⃣\tSUM\t ➕")
print("2️⃣\tDEVIDE\t ➗")
print("3️⃣\tMULTIPLY ✖️")
print("4️⃣\tSUBTRACT ➖")
print("PLEASE SELECT AN OPTION BETWEEN -\t1️⃣\t2️⃣\t3️⃣\t4️⃣")
print("⤵️")
XDA = input()



#do not change anything which is down bellow(🔻)

if XDA == '1':
    x = input("PLEASE WRITE YOUR FIRST NUMBER ➡️")
    Y = input("AND WHAT IS THE SECOND NUMBER? ")
    print("SUM OF THE TWO NUMBER IS\t", + str(float(X)) + str(float(Y)))
elif XDA == '2':
    x = input("PLEASE WRITE YOUR FIRST NUMBER ➡️")
    Y = input("AND WHAT IS THE SECOND NUMBER? ")
    print("DEVIDE OF THE TWO NUMBER IS\t", + str(int(X)) / str(int(Y)))
elif XDA == '3':
    x = input("PLEASE WRITE YOUR FIRST NUMBER ➡️")
    Y = input("AND WHAT IS THE SECOND NUMBER? ")
    print("MULTIPLY OF THE TWO NUMBER IS\t", + str(int(X)) * str(int(Y)))
elif XDA == '4':
    x = input("PLEASE WRITE YOUR FIRST NUMBER ➡️  ")
    Y = input("AND WHAT IS THE SECOND NUMBER? ")
    print("SUBTRACT OF THE TWO NUMBER IS", + str(int(X)) - str(int(Y)))
else:
    print("TO USE THE CALCULATOR RE RUN THE CODE\n\t\tGOOD-BYE")
