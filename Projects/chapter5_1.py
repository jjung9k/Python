# def return_test():
#     print("A 위치입니다")
#     return
#     pritn("B 위치입니다")
# return_test()
# print()

# #괄호가 없는 튜플
# [a, b]= [10, 20]
# (c, d)= [10, 20]
# [ e, f, g ]= [50, 100, 150]

# print("a: ", a)
# print("b: ", b)
# print("c: ", c)
# print("d: ", d)
# print("e: ", e, "\nf: ", f, "\ng: ", g)
# print()

# tuple_t = 10, 20, 30, 40
# print("# 괄호가 없는 튜플의 값과 자료형 출력")
# print("tuple_t: ", tuple_t)
# print("type(tuple_t): ", type(tuple_t))
# print()

# a, b, c = 10, 20, 30
# print("# 괄호가 없는 튜플을 활용한 할당")
# print("a: ", a, "b: ", b, "c: ", c)
# print()

# # 변수의 값을 교환하는 튜플
# a, b = 30, 40

# print("# 교환 전 값")
# print("a: ", a)
# print("b: ", b)
# print()

# a, b= b, a

# print("# 교환 후 값")
# print("a: ", a)
# print("b: ", b)
# print()

# 여러 개의 값 리턴하기.
def test():
    return (10, 20)

a, b= test()
print("a: ", a)
print("b: ", b)
print()
# 함수의 매개변수로 함수 전달하기
def call_10_times(f):
    for i in range(10):
        f()

def print_hello():
    print("안녕하세요.")
# 조합하기
call_10_times(print_hello) # 매개변수로 함수를 전달함
print()

# map() 함수와 filter() 함수
def power(item):
    return item * item
def under_3(item):
    return item < 3
list_input_a= [1,2,3,4,5]
output_a= map(power, list_input_a)
print("map(power, list_input_a): ", output_a)
print("map(power, list_input_a: ", list(output_a))
print()

output_b = filter(under_3, list_input_a)
print("filter(under_3, list_input_a: ", output_b)
print("filter(under_3, list_input_a: ", list(output_b))
print()

power = lambda x: x * x
under_3 = lambda x: x < 3

list_input_a= [1,2,3,4,5]

output_a = map(power, list_input_a)
print("# map()함수의 실행 결과")
print("map(power, list_input_a: ", output_a)
print("map(power, list_input_a: ", list(output_a))
print()

#람다는 함수를 짧게 쓸 수 있는 파이썬의 특별한 문법이다.
#튜플은 요소를 수정할 수 없는 파이썬의 특별한 문법. 괄호를 생략해서 다양하게 활용할 수 있습니다.

numbers = list(range(1, 10 + 1))
print(" ## 홀수만 추출하기")
print(list(filter( lambda x: x %2 == 1 , numbers)))
print()

print(" ## 3 이상, 7 미만 추출하기")
print(list(filter(lambda x: 3<= x < 7, numbers)))
print()

print(' ## 제곱해서 50 미만 추출하기')
print(list(filter(lambda x: x **2 < 50, numbers)))
print()
