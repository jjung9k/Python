# 기본적인 함수
# def name_time():
#     print("안녕하세요.")
#     print("반갑습니다.")
#     print("저는 강중구라고 합니다.")

# name_time()
# print()
# #매개변수의 기본
# def name_times(value, n):  # 괄호 내부에 value와 n 이라는 식별자를 입력! 이게 매개변수가 된다.
#     for i in range(n):
#         print(value)

# name_times("안녕하세요~", 3)
# print()

# #가변 매개변수 함수
# def name_times(n, *values): # n번을 반복한다. 매개변수는 n, 매개변수*values는 리스트처럼 사용
#     for i in range(n):
#         for value in values:
#             print(value)

#         print()

# name_times(3, "안녕하세요", '즐거운', '파이썬 프로그래밍') # 가변 매개변수 뒤에는 일반 매개변수가 올수가 없다. 

#기본 매개변수 함수
def output_times(value, n=6): # value 는 '가변 매개변수' 입니다.
    for i in range(n):
        print(value)
output_times("Hello~")
print()
# 기본 매개변수
def output_times(value, n=2):
    for i in range(n):
        print(value)

output_times("안뇽하세요~")
print()
#키워드 매개변수 : 매개변수 이름을 지정해서 입력하는 매개변수를 키워드 매개변수라고 한다
def name_times(*values, n=2):
    for i in range(n):
        for value in values:
            print(value)
        print()
name_times('안녕하세요', '즐거운', '파이썬프로그래밍', n=3)
print()
#여러 함수 호출 형태
def test(a, b=10, c=100):
    print( a + b + c )

test(10, 20, 30) # 일반매개변수는 숫자나 문자를 필수로 입력해야 하고, 순서대로 입력해야 된다
test(a=10, b=100, c=200) # 키워드 매개변수는 필요한 매개 변수값만 입력해도 되고, 순서도 원하는대로 입력할 수 있다
test(c=10, a=100, b=200)
test(10, c=200)
print()
#자료없이 리턴하기
def return_t():
    print('A 위치입니다.')
    return
    print('B 위치입니다.')
return_t()
print()
# 자료와 함께 리턴하기
# def return_t():
#     return 100
# value = return_t()
# print(value)
# print()
# # 아무것도 리턴하지 않았을 때의 리턴값
# def return_t():
#     return
# value = return_t()
# print(value)
# print()
#범위 내부의 정수를 모두 더하는 함수
def sum_all(start, end):
    output = 0
    for i in range(start, end + 1):
        output += i
    return output

print("0 to 100  : ", sum_all(0, 100))
print("0 to 1000 : ", sum_all(0, 1000))
print("0 to 100  : ", sum_all(50, 100))
print("0 to 1000 : ", sum_all(500, 1000))
print()
#기본 매개변수와 키워드 매개변수를 활용해 범위의 정수를 더하는 함수
def sum_all(start=0, end=100, step=1):
    output = 0
    for i in range(start, end + 1, step):
        output += i
    return output

print("A: ", sum_all(0, 100, 10))
print("A: ", sum_all(end=100))
print("A: ", sum_all(end=100, step=2))
print()

def f(x):
    return 2 * x + 1 
print(f(10))

def f(x):
    return x ** 2 + 2 * x +1 
print(f(10))






