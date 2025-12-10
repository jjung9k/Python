# 2. 반복문: while, for

# 1) while
# a = 0      # 변수
# while(a<3):     # 조건 설정
#     print('aaa')
#     # 조건에 사용한 변수의 값을 변경해 보기
#     # a=a+1  # 이렇게 제어 변수를 사용한다. 
#     a+=1
# print()

# # 특정 조건에 도달할 때까지 반복수행해야 할때.. 많이 사용함.
# # ex) 게임할때.. level 이 있는데 10을 넘어야 사냥을 갈 수 있다고 할때...
# # 레벨을 높이기위해 훈련을 해야함... 한번 훈련할때 마다 레벨 1씩 up이 되는....


# level = 5   #변수값 설정

# while(level<10):                      # 반복 조건 설정 (반복에 횟수는 여기 적힌  숫자가 아님!!) 
#     print('훈련!! 레벨업 해야 돼!!', level)
#     level = level + 1

# print('전투 참여') #실행문
# print("End")  # 실행문
# print()

# while문을 이용한 반복의 횟수는 하나의 코드만으로 결정되지 않음.
# 1) 제어변수 초기값, 2) 제어 조건, 3) 제어변수연산..을 모두 고려하여 결정하게 된다.

# "Hello"라는 글씨를 화면에 5번 출력하는 프로그램을 만들어 보세요.

# a = 0
# while(a<5):
#     print('Hello')
#     a+=1

# print('End')
# print()

# a = 0
# while(a<10):
#     print('Hello')
#     a+=2
# print('END')
# print()

# a = 5
# while(a<10):
#     print('Hello')
#     a+=1
# print('end')
# print()

# a = 5
# while(a>0):
#     print('Hello')
#     a-=1
# print('End')

# 만약. 판단이 안서면 ... 초기값 0. 조건은 < 횟수. 연산은 +=1

# 반복문의 실행문 영역에 print()만 사용할 수 있는 것은 아님. 어떤 코드든 가능함.
# 예시) 사용자로부터 정수를 5번 입력받으면서 짝수/홀수 인지를 출력해 주는 프로그램(아래 손코딩 참조)

# a=0
# while(a<5):
#     num= input('숫자 입력: ')  #키보드의 입력은 무조건 문자열 데이터로 인식함. 50을 입력하면 '50'
#     num=int(num)    #'50' --> 50 로 숫자 변환
#     if num%2== 0 :
#         print('짝수입니다')
#     else: 
#         print('홀수입니다')
#     a+=1
# print('End')

# 예2) 사용자로부터 정수를 5번 입력 받으면서 그 값들을 모두 더한 누적값을 출력하기.
# total = 0

# a=0
# while(a<5):
#     num= int(input("숫자 입력: "))
#     total= total+num   #누적 연산
#     a+=1

# print('입력된 정수의 총합은: ', total)
# print()

# 누적합의 구하는 방법을 문자열에 적용하면.. 문자열을 결합하여 새로운 긴 문자열을 만드는 방법으로 활용할 수 있음.
ss=""
ss=ss+"aaa"  #"aaa"
ss=ss+",bbb"  #"aaa, bbb"
ss=ss+",ccc"  #"aaa, bbb,ccc"
print(ss)
print()

# 반복에 사용했던 

n=0
while(n<5):
    print(n)
    n+=1
print()

# 이 제어변수를 단지 출력하는 것이 아니라 다른 변수와의

dan=4
n=1
while(n<10):
    print(dan, 'x', n, '=', dan*n)
    n+=1
print()

#조건식에 사용하는 값을 변수가 가지 값으로 지정하는 것도
num= 6
num= input()
a=0
while( a<num ):
    print('nice')
    a+=1
print()

# ()는 생략가능
a=0
while a<10: 
    print('good')
    a+=3

print(a)
