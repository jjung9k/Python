# 제어문 -- 프로그램의 진행 순서를 제어하는 문법
# 1. 조건문 if, if-else, if - elif
# 1) if

age = 19
if ( age<20 ):
    print('미성년자군요. 시청에 주의하세요')
    print('다른 콘텐츠를 시청하세요.')

print('안녕하세요. 넷플릭스 입니다.')
print()
#-------------------------------------------

#2) if - else
age = 25
if(age>=20):
    print("환영합니다. 문나이트 입니다.")
    print("신나게 노세요~")

    # 영역 안에 출력기능만 사용가능한 것은 아님.
    # 어떤 코드든 가능.
    # n= int(input('숫자입력: ')
    n=10
    n+= 2
    print('n:', n)
else:
    print("입장이 불가합니다.")
    print("더 커서 와~~")
print('-'*30)
print()

# 3) 중첩 if
age = 25

if(age<20):
    print('꺼져!')

    if(age>18):
        print("뒷문으로 와~")
else:
    print("환영합니다. 문나이트입니다.")

    gender='female'
    if(gender=='female'):
        print('할인해 줍니다.^^')
    else:
        print('정가 그대로입니다..ㅜㅜ')
    print('필요한거 있으면 "찬호박"을 찾아주세요') 
print()
print("~~"*20)
print()

# 4) if - elif  (중첩 if의 축약 문법)
# 예) 시험점수를 입력하면 학점을 계산해서 출력하여 주는 프로그램
score = 85
if( 90 <= score <= 100):
    print('A학점 입니다.')
    print('아주 우수합니다.')
elif(80<=score<90):
    print('B학점입니다.', '\n우수합니다')
elif(70<=score<80):
    print('C학점입니다.', '\n준수합니다.')
elif(60<=score<70):
    print('D학점입니다.', '분발하세요.')
elif(0<=score<60):
    print('F학점입니다.', '재수강입니다.')
else:
    print('잘못 입력했습니다.')
    
#5) 조건이 2개 이상인 경우가 있음. [ㅣ2개 이상의 변수의 조건을 묶어서 비교해야 하는 경우] - 비교연산을 묶어주는 연산자[논리 연산자]

#5.1) and를 사용하는 경우 [점수 90이상이고, 결석이 1개 이하일때는 A+ 부여]
score=95         #점수  
absent_days = 1  #결석일수
if( score>=90 and absent_days<=1):
    print('A+학점입니다. 성실하면서.. 성적도 우수합니다. \n최우수 학생입니다.')
else:
    print('당신은 최우수 학생은 아닙니다.') 
print()

#5.2) or를 사용하는 경우 [이벤트 당첨. 당첨조건 : 리뷰를 작성했는데 특정단어(좋아요)가 포함 되어 있거나 최소 20글자 이상 작성한 리뷰]
review= '오늘 신발이 도착했어요.'  #변수는 2번 중복이 안 되어서 첫번째 변수는 의미 없어짐
review= '오늘 신발이 도착했어요. 완전좋아요.'
review= '오늘 신발이 도착했어요. 이거 편하네요. 그리고 빨리 도착 했어요. 만족합니다.'
if( ('좋아요' in review) or len(review)>=20):
    print('이벤트 당첨!! 축하드립니다.')
else:
    print("탈락!! 원하는 단어가 없거나 글자수가 너무 적어요.")
print()

#5.3) not을 사용하는 경우 [ 필수는 아니지만.. 코드를 해독할때... 사람이 생각하는데로... 써져 있어서 선호함.]
age=15
if(not age>20):
    print('미성년')
else:
    print('성인')

print()

# 강아지 키우는 게임
print("@강아지 키우기@")
print("----------------")
print("1. 밥먹기")
print("2. 산책하기")
print("3. 목욕하기")
print("---------------")
menu= input('메뉴선택: ')
print()

#메뉴 선택에 따라 다른 동작

if(menu=='1'):
    print('아구아구 맛있다.')
elif(menu=='2'):
    print('와우 신난다~')
elif(menu=='3'):
    print('으아~~ 짜증나')
elif(menu=='4'):
    print('잘못된 메뉴를 선택 했습니다.')
print()

#python 3.10버전에서 새로 도입된 문법 match-case [다른 언어에서 사용하는 swithch-case문] -- 비교연산을 가독성 좋게 해 주는 문법
match menu:
    case '1'| '밥먹기':   # 비트 연산자
        print('아구아구~ 맛있다.')
    case '2':
        print('와우 신난다~')
    case '3' | '4' | '7':  # 비트 연산자 
        print('으아!! 짜증!!~~')
    case _:
        print('잘못된 메뉴 번호를 입력했습니다.')
print()
print("-------------------")
print()

#7) 특이한 키워드 pass --- 미완성 작업중일때-- 사용
a= 100
if a<100:
    print("aaa")
else:
    #여기 작업을 좀 나중에... 다른 작업 후에.. 완료하고 싶을때...
    print("bbb")

# 9) 조건의 실행문이 한줄이면... 코드도 한줄로 입력해도 됨.
#1] if
age= 25
if age>20: print('adult')

# 2] if - else [순서가 조금 이상]
#원래 모습
number= 10
if number%2==0:
    print('짝수')
else:
    print('홀수')

# one line if [순서가 이상하다... 콜론도 없음] 실행문A if() else 실행문B
print('짝수') if number%2==0 else print('홀수')

#3] if elif else
munu=1
print('Hello') if menu==1 else print('nice') if menu==2 else print('good')

#10) 삼항연산자 [ 다른 언어 및 프로그램에 존재하는 age>20? 'A':'B' 삼항연산자를 one line if 문으로 대응함]

# 예) 사용자가 정수 2개를 입력하면.. 그 값 중에 큰 값이 max 라는 변수에 저장되도록...
num1= 10
num2= 5

#num1과 num2 중에 큰 값을 max 변수에 대입
if num1>num2:
    max= num1
else:
    max= num2
print('둘 중에 큰 값은:', max)

# 삼항연산자 대응문법으로 처리
max= num1 if(num1>num2) else num2

#예2) 학점 출력을 삼항연산자로.. 입력.. ternary operator
scroe= 85
grade= 'A학점' if(score>=90) else 'B학점' if(score>=80) else 'c학점' if(score>=70) else 'D학점' if(score>=60) else 'F학점'
print('당신의 학점은: ', grade)
print()

#10) 파이썬은 0과 같이 값이 없는 것을 제외하고는 모두 참(True)으로 해석..된다. 
data=10   #True
data=0    #Flase
data='aaa' #T
data=''   #F
data='  ' #T
data=[10,20,30] #T
data=[] #F
if data:
    print('hello')

# 사용자가 값을 입력을 해야 하는데.. 안하고 그냥 엔터 눌렀을 경우
text= intput('글씨를 입력하세요:')

# 사용자가 입력을 했을 경우.. 를 대응하기 위해
if not text:
    print('입력해 주세요!!!!')
else:
    print('입력된 글씨는 : ', text)

# 사용자가 입력을 안 했을 경우.. 를 대응하기 위해
if not text:
    print('입력해 주세요!!!!')
else:
    print('입력된 글씨는 : ', text)
print('-----------------------')

# 조건 사용할때 주의할 점.
aa= 'Hello'

n=5
if n<10:
    aa='nice'

print('aa : ', aa )

tt=None
n=5
if n<10:
    tt='nice' #이때 처음 만들어짐
    print('안: ', tt)
if not tt: print('밖:', tt)