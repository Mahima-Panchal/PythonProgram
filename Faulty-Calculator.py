# Design a calculator which will correctly solve all the problems except the following one :
# 45 * 3 = 555, 56+9=77, 56/6=4
# Your program should the operator and the two numbers as input from the  user
# and  then return the result.

num1 = int(input("Enter the First Number:: \n"))
opr = input("Enter The Operator [+, -, *, /]:: \n")
num2 = int(input("Enter the Second Number:: \n"))
if opr == '+':
    if num1 == 56 and num2 == 9:
        print(num1, opr, num2, "= 77")
    else:
        print(num1, opr, num2, "=", num1+num2)
elif opr == '-':
    print(num1, opr, num2, "=", num1-num2)
elif opr == '*':
    if num1 == 45 and num2 == 3:
        print(num1, opr, num2, "= 555")
    else:
        print(num1, opr, num2, "=", num1*num2)
elif opr == '/':
    if num1 == 56 and num2 == 6:
        print(num1, opr, num2, "= 4")
    else:
        print(num1, opr, num2, "=", num1*num2)
else:
    print("Enter The Valid Data.")
