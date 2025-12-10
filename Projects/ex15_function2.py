# 함수 2부 수업

# 1. 재귀호출 - 어떤 함수가 본인 함수를 다시 호출하는 것.
# 함수 

def aaa():
    print('aaa.....')
aaa()
print('Hello')
aaa()
for i in range(3):
    aaa()
print()

#기본적으로 함수안에서 다른 함ㅎ수를 호출하는 것은 가능함.
def bbb():
    print('This is bbb function')
    aaa() #다른 함수 호출
    print('nice to meet you')

bbb()
print()

#함수식별자() 만 쓰면 그 함수의 코드가 실행 됨.
#그렇기에 본인 함수안에서 본인함수를 다시 호출하는 것도 문법적으로 문제가 없음.
def ccc():
    print('ccc!!!!!!!!!!!!!')
    aaa()
    bbb()
    # ccc() # 본인 함수를 호출하면 본인함수의 코드가 다시 실행 됨. 마치... 무한반복..
    # 결국 에러발행 함. 무한하게 함수코드영역을 메모리에 할당하기에 메모리 부족문제가 발생하여 파이썬 인터프리터가 자동
ccc()
print()

#본인함수가 본인함수를 호출하는 것을 '재귀호출'이라고 부르며 무한하게 사용은 하지 않고, 특정 조건이 되면 더이상 호출하지 않도록 코딩하여 사용함.
def ddd(n):
    if n==0: return
    print('nice', n)
    ddd(n-1)  #recursive call(재귀호출)
    print('end', n)

ddd(5)
print()

# 재귀호출은 연속적으로 유사작업(같은 기능)을 반복적으로 수행할때 효과적이다. 
# 대표적으로.. 5! 팩토리얼연산.. 피보나치 수열... 프렉탈 패턴 같은.. 특정 패턴의 반복수행에 사용 됨.

def factorial(n):
    output = 1
    for i in range(1, n + 1):
        output *= i
    return output

print("1!:", factorial(1))
print("2!:", factorial(2))
print("3!:", factorial(3))
print("4!:", factorial(4))
print("5!:", factorial(5))
print()


