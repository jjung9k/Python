# 리스트 평탄화하기(1)
def flatten(data):
    out = []
    for item in data:
        if type(item) == list:
            out += item
        else:
            out.append(item)
    return out

ex = [[1,2,3], [ 4,[5,6],7,[8,9] ]]
print('원본: ', ex)
print('변환: ', flatten(ex))
print()
#----------------------------------------------------
# 리스트 평탄화하기(2)
def flatten(data):
    out = []
    for item in data:
        if type(item) == list:
            out += flatten(item)  # 플래턴() 함수를 재귀적으로 호출한다.
        else:
            out.append(item)
    return out

ex= [[1,2,3], [ 4,[5,6],7,[8,9] ]]
print('원본: ', ex)
print('변환: ', flatten(ex))   # 리스트가 복잡하게 중첩되어 있어도 문제없이 평탄화 하는 함수를 만들수 있다.
print()

#리스트와 튜플의 특이한 사용
[a, b] = [10, 20]
(c, d) = (10, 20)

print('a: ', a)
print('b: ', b)
print('c: ', c)
print('d: ', d)
print()

#괄호가 없는 튜플
tuple_test = 10, 20, 30, 40
print('# 괄호가 없는 튜플의 값 출력')
print('- 튜플 테스트: ', tuple_test)
print()
a, b, c = 10, 20, 30
print('# 괄호가 없는 튜플을 활용한 할당')
print('a: ', a)
print('b: ', b)
print('c: ', c)
print()

#변수의 값을 교환하는 튜플들
a, b = 10, 20

print("# 교환 전 값")
print('a: ', a)
print('b: ', b)
print()

a, b = b, a
print("# 교환 후 값")
print('a: ', a)
print('b: ', b)
print()

# 여러개의 값 리턴하기
def test():
    return(10, 20)
a, b = test()
print("# 여러개의 값 리턴")
print('a: ', a)
print('b: ', b)
print()

#함수의 매개변수로 함수 전달하기
def call_10_times(func):  #매개함수로 받은 함수를 10번 호출하는 함수
    for i in range(10):
        func()
def print_hello():
    print("안녕하세요")

call_10_times(print_hello)  #매개변수로 함수를 전달!
print()

#기본 매개변수
def print_n_times(value, n=2):
    for i in range(n):
        print(value)

print_n_times("안녕하세요")


