# 함수(function 기능) : 특정 기능을 수행하는 코드를 모아 놓은 코드영역
# 예) 로그인함수(==로그인 기능 코드들), 회원가입함수(==회원가입 코드들 영역), max함수(==최대값 구해주는 기능 코드들)

# [ 특정 기능을 작성한 코드 영역을 필요할때 마다 언제든 호출(call)하여 그 코드영역이 실행되도록...]
# 파이썬 함수의 종류
# 1. 표준(내장) 함수 : 이미 파이썬에서 만들어서 내장해 놓은 함수들 print(), input(), len(), max() .....
# 2. 외부 함수: 기존 개발자 또는 업체들에서 만들어 라이브러리로 제공하는 함수들. 내장되어 있지 않아서 그냥 사용불가능.대신 그 모듈(함수들을 모아놓은 폴더)을 파일에 삽입(import)하여 불러 사용함. import datetime
# 3. 개발자 정의 함수 (오늘 수업)


# 코드가 써있는 영역을 구분하기 위해 보통 함수의 이름을 영어로 작성. (동사 v)
# 함수 이름(식별자) 옆에 소괄호 ()가 반드시 있어야 함. 이를 통해 변수와 구별함
# age ---> 변수
# login() ---> 함수

#1. 함수 정의 문법 [define]
def show (): 
    print('show function...hello')
    #코드 영역에 여러줄 코드 가능
    print('good')

# 함수를 정의했다고 해서 코드가 실행되는 것은 아님. 함수를 사용하겠다고 호출해야 그 영역의 코드들이 실행됨
print('함수 호출 연습') #들여쓰기가 아닌 출력문이 먼저 실행 된다.
# 함수 호출 founction call
show()
# 필요할때 언제든 다시 함수를 호출할 수 있음. 그럼 그 코드영역이 다시 실행 됨.
show()
print()

# 매번 함수 호출할때 마다 같은 글씨만 출력되는 기능은 효용성이 약해보임. 내가 전달한 값을 출력해주는 기능이 필요한 경우도 있음.
#2. 함수를 만들때 값을 전달받는 함수 만들기
def show_name(name): # name 처럼 소괄호() 안에 전달된 값을 받기 위한 변수를 '매개변수'라고 부름. 영어로는 파라미터(parameter)라고 함.
    print('welcome!', name)

# 함수를 호출하면서 매개변수에 값 전달.... 
show_name('joongku')
show_name('Andy')
print()
# 매개변수는 여러개 일수도 있음.
def output(a, b):
    print('a: ', a)
    print('b: ', b)
output(10, 20)
output(100,     3000)
# 사용할때 주의할점. 함수호출할때 매개변수의 갯수만큼 값을 줘야만 함. 파라미터 갯수만큼 반드시 값을 전달해야만 함... 다르면 에러~
# 경우에 따라서는 값 전달하면 그 값을 보여주고, 아니면 기본값 보여줘... 이를 위한 문법 [기본값 지정]
print()

#3. 함수 파라미터의 default value 지정.
def display(a=1, b=2):
    print('a의 값: ', a)
    print('b의 값: ', b)

display(100, 200)
display(100) # a=100 , b는 기본값
display()  # a,b 모두 값이 기본으로 출력 된다.
# 근데.. 값 1개 줄건데.. b에게 [ML 함수들 사용할때 꽤 많이 사용함.]
display(b=1000)
display(a=50, b=30)
print()

def display2(a, b=2):
    print(a, b)

#display2() # error
display2(10)
display2(10,20)
#display2(b=50)  #error
show_name('Kang')
output(3, 5)
display(b=2000)
display2(1000, b=20000)


# 기능을 만들다보면 .. 전달값이 몇개인지 특정하기 어려운 경우가 있음.
# 예) 전달받은 모든 값 출력.. 모든 값 덧셈....(총합) 구하기
# 해결방법1) 여러개의 값을 받기 위해 리스트 [] 대괄호 1개로 받기... 
def cal_total(number_list):
    print('전달받은 값의 총합: ', sum(number_list))

cal_total([10, 20])
cal_total([10,20,30,40,50])
cal_total([10,20,30,40, 50, 60, 70])
#cal_total(10,20,30) #error

#4. 매개변수의 길이가 가변적인 파라미터 variable length arguments [가변 파라미터]
def nice( *values ): # 보기에는 그냥 변수 1개로 보이지만.. 사실 내부에서는 ""리스트로 만들어 줌""  *를 꼭 앞에 붙여야 됨.
    print('전달 받은 값의 개수 : ', len(values))
    for v in values:
        print(v)

nice()
nice(10)
nice(10, 20)
print()

# 표준 내장 함수 중에서 가변파라미터를 사용하는 함수

m = max(40,50,60,70)  #파라미터에 값 4개를 전달
print(m)
print()
#----------------------------------------

#함수를 정의할때 유의할 점.. 같은 이름의 함수를 또 정의하면??
def aaa():
    print('aaa function')
aaa()

def aaa():
    print('다시만든 aaa function')
aaa()

def aaa(num):
    print('aaa num:', num)

aaa(10)
# aaa() #error


# 그래서 주의... 여러분은 모든 내장함수의 이름을 외우지 못함.
# 하필.. 내장함수와 같은 이름의 함수를 만드는 경우가 있을수 있음.

#변수 이름도 식별자여서.. 내장함수명을 변수명으로 덮어지기도 함.
print()
# 함수의 호출문이.. 함수 정의보다 먼저 되면 안된다..!!
#gg() #error

def gg():
    print('gggggg')
gg()
print()

#5. 리턴을 해주는 함수... 함수 안에 print()로 출력만 하는게 아니라... 연산결과를 함수로 호출하는 쪽으로 되돌려 주는 문법
def aaa():
    return 10 #10이라는 값을 호출하는 쪽으로 돌려주는 기능함수


#리턴받는 모습을 처음 보는 것이 아님.. 내장함수 사용할때...
#num1= input()
#m= max(10, 30, 50, 50, 40)

# 매번 같은 값만 리턴되면 효용가치가 떨어지는 기능임
# 2개의 정수를 전달하면 덧셈의 결과를 계산해서 리턴해주는 기능(함수)
def add(a, b):
    x = a + b
    return x  # 리턴을 사용하게 되면,, 실행을 해서 뭔가 가지고 오는거다.. 

num= add(3, 5)
print(num)

num= add(8,6)
print(num/2)
#return을 할때,, 값이 없이 사용하는 것도 가능함.
def ccc():
    print('ccc function')
    return # 이 글씨를 만나면 되돌아 가라고 하는 것이어서 이 함수의 코드영역이 종료되는 것을 의미함.
    print('zzz')  #여긴 실행 안됨.

ccc()

def ddd(n):
    # 음수이면 출력안되도록 하고 싶을때...
    print(n)
print()

# 만약, 






#일반변수 대입도 한번에 여러개 대입 되었었음.
n1, n2= 100, 200
#n1, n2, n3= 1,2 # error

a= 1000, 2000 # a 변수가 여러개의 값을 가진 것이 아님. 튜플 1개
print(a)
print(type(a))
print()



def hhh():
    return('san', 'robin', 'hong')

name_list= hhh()
print(name_list)  # 결과값: ('san', 'robin', 'hong')
print(len(name_list)) # 3개 요소
print(len(name_list[0])) # 3개 문자
print(len(name_list[1])) # 5개 문자
print(len(name_list[2])) # 4개 문자 
print()
# 리턴된 리스트1개를 분해하여 요소별로 변수에 바로 대입
name1, name2, name3= hhh()
print(name1.upper()) # upper는 대문자로 바꿀때 사용한다
print(name2.upper())
print(name3.upper())
print()

#[별외.] 지역변수(local variale)와 전역변수(global varialbe)에 대한 이해..
def mmm():
    age= 20 #지역변수 ->> 함수 안에서 처음 만들어진 변수: 이 지역안에서만 인식 가능하다
    print('나이: ', age)
mmm()
print()
#함수의 지역변수는 밖에서 사용불가능.
# print('밖: ', age) #error

#함수 밖에 만든 변수는 전역변수이다. 
name= 'park'
def nnn():
    # 함수안에서 변수값을 변경하려는 코드를 쓰면..새로운 지역변수 생성문법으로 인식함
    name='kim' #새로운 지역변수를 만들었다고 생각함.
    print('함수 안 : ', name) #밖에서 만들어진 변수를 사용할 수 있음(이때 전역변수라고 부른다)

nnn()
print('함수 밖 :', name) # 여기서도 사용가능. 그래서 전역변수라고 부름.
# 그래서 함수안에서 전역변수의 값을 변경하고 싶다면... 내가 사용하는 변수가 전역변수임을 명시적으로 알려줘야 함.
def ttt():
    global name # 이 함수 안에서 name 변수는 밖에 있는 전역변수를 사용할 것이라고 명시!!
    name='lee'
    print('-함수 안- : ', name)

ttt()
print('-함수 밖- : ', name, end='\n')
print()




