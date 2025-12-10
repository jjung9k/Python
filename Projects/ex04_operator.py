# 연산자 : 산술, 비교, 논리, 비트, 복합대입, 형변환

#1. 산술
a= 10
b = 3

print( a + b )
print( a - b )
print( a * b )
print( a / b )

print( a % b )  #나머지값 연산자
print( a // b ) #몫, //는 띄워쓰기하면 안 됨!!

# 나눗셈의 몫, 나머지 값을 한번에 연산하여 결과를 주는 기능함수를 제공함. divmod()
x, y=divmod(a,b)
print('몫:', x)
print('나머지 : ', y)

# 부호 변경 연산자 - [단항 연산자]
c= 10
print( -c )
c = -10
print( -c )

# 제곱연산 연산자
a = 4
print( a**2 ) #4의 제곱
print( a**4) #4의 세제곱
print( a**(1/2)) # 4에 제곱근 [루트]
print()

#2. 비교 연산자
a= 10
b= 4

print( a > b ) #True
print ( a < b )
print( a >= b )
print( a <= b )
print ( a == b )
print ( a != b ) # !는 부정적인 의미로 쓰인다.

# a 변수가 특정 범위안에 있는지.. 여부
# a가 0~100 사이의 숫자인가...
print( 0 < a < 100 )
a=150
print( 0 < a < 100 )
# 나이가 20대 인가요?
age = 20
print( 20 <= age < 30 ) 

#3. 논리 연산자 : and, or, not
#하나의 변수에 대한 범위조건이 아니라.. 2개 변수의 조건을 동시에 체크하는 경우도 많음.
#[예] (놀이기구 탈때..) 나이가 10살이상이고.. 키가 150이상인 조건만.. 허용...
age = 15
height = 160
print(age >= 10 and height >= 150 ) # 두 비교연산의 결과가 모두 true 인 경우만. True 가 되는 논리연산

#나이가 10살 이하이거나... 키가 150보다 작다면... 
print( age < 10 or height < 150 ) #두 비교연산의 결과 중 하나라도 true 면 'True' 결과를 주는 논리연산

# 미성년자가 아니냐.. 이라는 조건을 넣을 경우...
age = 25
print( age>=20 ) # 이렇게 써도 됨..(성인이냐?)

print( not age<20 )

#비트 연산자(거의 사용안함. 한번만 살펴보기..) 계산방식 -- 연산에 사용된 피연산자들을 2진수로 바꾸어.. 각 비트자리끼리 연산수행
print( 7 & 4 ) # and 비트연산
print( 7 | 4 ) # or 비트연산
print( 7 ^ 4 ) # Exclusive or 비트연산
print( 8  >> 2 ) # shift 연산.. 비트를 오른쪽으로 2칸 밀기.
print( 8  << 2 ) 
print( ~ 10) # 0->1, 1->0  (숫자의 부호도 바뀌어 버림)
print( )

#5. 복합대입 연산자 ( 산술 + 대입 )
a= 10
#a = int( input('입력:'))   # integer : 정수 
#a 변수가 가진 값을 1 씩 증가시켜라... 요청

a+1 #덧셈을 하지만,, 그 결과가 a 변수에 대입되진 않음.
print( 'a:', a )
a= 20
a= a+1
print( 'a:', a ) #21

a= a+2
print( 'a:', a ) #23

#증가 되려면.. 연산한 결과를 다시 a변수에 대입해야 함.
a = a + 1

character_age= 20
print("age:", character_age)

character_age= character_age + 1
print("age:", character_age)

#변수명을 2번씩 쓰는게 은근 짜증 남..
character_age += 1
print("age:", character_age)

character_age += 5
print("age:", character_age)

character_age -= 3
print("age:", character_age)

character_age *= 10
print("age:", character_age)

#순서는 바꿀 수 없음.
character_age =+2 #양수 2
print("age:", character_age)

character_age =-2 #음수 2
print("age:", character_age)
print()

#6. 형변환 연산자(기능함수) [ Type casting ]
a= '10'
print( type(a))


a = int(a)
print( type(a))
print( a + 3  )

a= '3.14'
#print( int(a) + 5.12 ) #error
a = float(a)  #float: 실수(소수점이 있는 수)
print( a + 5.12  )

# str() 형변환 기능... 문자열로 변환
print( 5 + 3 ) #숫자 + 숫자 는 산술 더하기
print( str(5) + str(3) ) # 문자 + 문자  는 문자열결합 연산. '5'+'3' ==> '53'

#bool() : 단순히 'True' 문자열을 True 논리값으로 변환하는 것은 아님.
#파이썬은 값이 없는 것(0, "빈 글씨", [], None, Flase)을 제외하고 모두.. 참(True)이다. 
a = 'True'
print( type(a))

a= bool(a)
print( type(a))

a= 10
print( bool(a)) #True

a= 0
print( bool(a)) #False

a= -5
print(bool(a)) #True

a="Hello"
print( bool(a)) #True

a=""
print( bool(a)) #True

a="  "
print( bool(a)) #False

a=None
print( bool(a))  #False

a= 0.0
print( bool(a)) #False

# 나중에 조건문 if 문법을 사용할때 조건에 대해 확인할 때... 이 개념을 사용함.
# 예) 엑셀파일을 읽어들여서.. 그 데이터를 출력할때..
#table = pandas.read_exe1('aaa.xls')
#if bool(table):
#       print("테이블 값 들 출력")
#else:
#       Print("테이블에 데이타가 없어요.. ")

#일반 산수에도 연산자 우선순위가 있듯이... 파이썬에도 존재함.
print( 3+5*6  ) # 더하기(+) 보다 곱하기(*)를 우선으로 연산한다.
print( (3+5)*6 ) # 우선순위 변경은 소괄호
 
#사실.. 아래 코드로 연산자 우선순위와 관련이 있는 내용.
num=3+6
print()

#프로그램에서 사용하는 대부분의 데이터는 문자열이 많음. [ 이름, 제목, 메모글, 리뷰, 아이디 ]
#문자열 데이터를 다루기 위한 연산자와 기능함수들... 소개

#1) 문자열 연사자 3개  +  *  []    대괄호>>인덱싱
#1] +결합연산자
print( 'aa'+ 'bb' )

#2] * 반복 연산자
print( 'aa' * 3) #aa를 3번 반복하여 문자열 생성
s= "Good"*5  # => "GoodGoodGoodGoodGood"
print( s )

#print( 'aa' - 'bb') #error
#print( 'aa' / 3) #error

#3] 문자열에 인덱싱.. 슬라이싱
s = "Hello world"
print( s )
#문자열(문자가 여러개인 것..)의 특정 위치 글자를 뽑아올 수 있음
print(  s[1]  ) #인덱스 번호(0번부터~)가 1번인 위치의 값..... 'e' 값이 나온다.
print(  s[1:7]  ) #1번부터 ~ 7번 전까지.. [1~6]의 글씨를 뽑아오기.
print( s[1:])  #1번부터 ~ 끝까지.. 출력
print( s[:7] ) # 처음부터 ~ 7번 전까지. [0~6]
print(  s[-1] )  # 뒤에서 첫번째 요소의 글씨...
print( s[-5]  ) # 뒤에서 5번째 요소의 글씨...
print(  s[-5:] ) # 뒤에서

# 2) 문자열이 가진 유용한 기능함수들() ...

#1] 문자열의 길이(글자수)를 알려주는 내장함수 len() : length
print( len(s) )

#2] '문자열데이터'.format() 기능... 특정서식모양을 만들어 사용하는 기능
money= 500
print(money, '만원')
print("{}만원".format(money))
name= "sam"
age= 20
print("이름:{}    나이: {}".format(name, age))

aaa= "{}님 반가워요".format(name)
print('만들어진 문자열:', aaa)
print("글자수는 : ", len(aaa))

#format() 의  {}에 들어갈 데이터의 종류를 미리 고정할 수 있음. 코드 실수 방지!
print("{}  {}".format(10, 'aaa'))
hour= 10
min= 12
sec=7
print("{:02d}:{:02d}:{:02d}".fotmat(hour,min,sec))
hour= 10
min= 12
sec=7



#정수일때.. 칸수 지정
print("[{}]".format(100))
print("[{:5d}]".format(100))
print("[{:05d}]".format(100))

#부호가 표기되고 싶다면
print("[{:+ d}]".format(30))
print("[{:+ d}]".format(-30))

#부호를 칸의 왼쪽끝으로 배치하기
print("[{:+5d}]",format(30))
print("[{:+5d}]".format(-30))

#실수일때.. 칸수 지정
print("{}".format(3.14))
print("{:f}".format(3.14)) # float을 쓰면 무조건 소수점 아래 6자리까지 출력 됨
print("{:10f}".format(3.14)) # 총10자리를 입력이 됨 # 출력값:[  3.140000]  -> 숫자는 뒤에서부터 출력됨.
#소수점 아래의 칸수를 지정
print("{:10.2f}".format(3.14))
print("{:.2f}".format(3.14))
#정수를 소수점으로 표시하기
print("{:.1f}".format(100)) # 출력값 : 100.0
#print("{:d}".format(3.14)) #error
#소수점이 필요하면 찍고.. 아니면 찍지 않았으면.. 좋겠다면...(정수인지 실수인지 모를때)
print("{:g}".format(100))
print("{:g}".format(3.14))  #제네레이터 :g를 쓰면 된다.

#문자열 일때.. 칸수 지정

print("이것은 [{}]입니다".format('aaa'))
print("이것은 [{:s}]입니다".format('aaa'))
print("이것은 [{:10s}]입니다".format('aaa'))    #문자는 왼쪽부터 출력 된다.
#남은 공간의 오른쪽으로 배치...
print("이것은[{:<}]" 입니다.)  #여기서부터 다시 메모 및 작성!!

#진법 표시
print("{:d}".format(10) )  #10진수 - decimal
print("{:o}".format(10) )  #8진수  - octal
print("{:x}".format(10) )  #16진수 - hexadecimal 
print("{:b}".format(10) )  #2진수  - binary

#파이썬 코드로 2진수, 8진수, 16진수를 표기해보기..
print("{:d}".format(0o10) )  #8진수 표기법 0o 
print("{:d}".format(0x10) )  #16진수 표기법 0o
print("{:d}".format(0b10) )  #2진수 표기법 0o

