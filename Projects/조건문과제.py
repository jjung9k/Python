# 과제1) 사용자로부터 정수 하나를 입력 받아서 정수의 절대값을 출력하는 프로그램을 작성. 하시오.
# num = int(input("정수를 입력하세요.: "))
# if num < 0:
#     ab = -num
# else:
#     ab = num
# print("절대값: ", ab)

# 과제2) 두 정수 중 작은 값 출력 하시요.
# a = int(input("첫번째 정수를 입력하시요: "))
# b = int(input("두번째 정수를 입력하시요: "))

# if a < b:
#     print("더 작은 값은: ", a)
# elif b < a:
#     print("더 작은 값은: ", b)
# else:
#     print("두 값이 같아요: ", a)
# print()

# 과제3) 사용자로부터 정수 3개를 입력 받아 정수형 변수 a, b, c 에 각각 저장한 후, 조건문을 사용하여 이들 변수 중 가장 큰 값을 가진
# 변수의 값을 max라는 이름의 정수형 변수에 대입하고 출력 하시요.
# a = int(input("첫번째 정수를 입력: "))
# b = int(input("두번째 정수를 입력: "))
# c = int(input("세번째 정수를 입력: "))
# max = a
# if b > max:
#     max = b
# if c > max:
#     max = c
# print("가장 큰 값은? ", max)
# print()

# 과제4) 두 개의 정수를 입력 받아서 두 수의 차를 출력하는 프로그램을 구현하시오. 단, 무조건 큰 수에서 작은 수를 뺀 결과를 출력해야 한다. 

a= int(input("첫번재 정수를 입력: "))
b= int(input("두번째 정수를 입력: "))
if a > b:
    result = a-b
else: 
    result = b-a
print(result)
print()




