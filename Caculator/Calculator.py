"""Made by Darkhost - 2016.06.11 """
def Plus(num, num1):
    print(num + num1)

def Minus(num, num1):
    print(num - num1)

def Multiply(num, num1):
    print(num*num1)

def Divided(num, num1):
    print(num / num1)

print("Calculator by Darkhost - Python Study")
first_num = int(input("첫번째 수를 입력하세요.\n"))
second_num = int(input("두번째 수를 입력하세요.\n"))
select = int(input("사용할 부호를 선택하세요.\n1. +\n2. -\n3. *\n4. /\n\n"))

if select == 1 :
    Plus(first_num, second_num)
elif select == 2 :
    Minus(first_num, second_num)
elif select == 3 :
    Multiply(first_num, second_num)
elif select == 4 :
    Divided(first_num, second_num)
else :
    print("잘못된 부호 입니다.")