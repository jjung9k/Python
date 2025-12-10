#하나의 py파일에 모든 코드와 기능을 작성하여 복잡함. 기능별로 관리거나 재사용하기 어려움.
# 모듈은 여러상수값이나 기능함수들을 가지고 있는 파일의 집합체임(일종의 폴더)

# 파이썬 모듈의 종류
# 1. 표준 모듈: 파이썬을 설치할때 같이 내장되어 설치된 모듈들.. 그래서 별도의 설치없이 그냥 import만 하면 됨(내장함수는 아님. import없이는 사용불가)
# 2. 외부 모듈 : 사용하려면 별도의 다운로드 및 설치작업이 요구되는 모듈들 [이런 외부모듈을 설치해 주는 프로그램 > pip(CLI

# 먼저 표준 모듈 중 활용이 많은 모듈들

#1. math 모듈: 수학적인 연산기능(함수)들을 모아 놓은 폴더 같은 모듈
import math #모듈 적용

print( math.sin(1) )
print( math.cos(1) )
print( math.log(1000, 10) ) # x, 밑수 ..[밑수를 몇승하면 x 값이 되는가]
print()
print( math.floor(3.7) ) #소수점 아래 내리기...
print( math.ceil(3.1) )  #소수점 아래 올리기...(소수점이 있으면 무조건 앞자리 올리기)
#반올림은..math 모듈이 아니라.. 표준함수에 존재함
print()
print( round(3.7) )
print( round(3.2) )

#1.1 모듈 사용할때 마다 모듈명. 쓰는거 은근 짜증난다. 모듈명이 길면 쓰기가 불편하다.
import math as m
print( m.pow(4,2) )  #pow(): 4의 2제곱
print()

#1.2 줄여쓰는 모듈명 조차도 짜증... 모듈명 없이 필요한 함수만 뽑아서 imprt 하는게 가능하다.
from math import floor, ceil 
#뽑아온 함수를 마치 내장함수인 것처럼.. 그냥 사용할 수 있다.
print( floor(2.5) )
print( ceil(2.5 ) )
#함수 말고 값도 있음
print(math.pi)
print()
#-----------------------------------

#2. ramdom 모듈: 랜덤값 생성. 관련 기능
import random

print( random.random())  #0.0000 ~ 0.999999..........
#만약 0~9 중의 하나의 숫자를 생성하려면..(정수만...)
num= math.floor(random.random() * 10)
print(num)
# 위 계산을 쉽게해 주는 기능함수가 존재함.
print(random.randrange(10)  ) #0~9   중에 랜덤으로 숫자 하나가 나옴
print(random.randrange(5, 16))  #5~15 중에 랜덤으로 숫자 하나가 나옴

aaa= [1,2,3,4,5]
print( random.choice(aaa) ) # 랜덤하게 값 1개를 출력
print( random.sample(aaa, 3)) # 임의값 3개를 출력 - 리스트로 리턴
print()

# [예] 로또 번호 추천
lotto= list( range(1, 46) ) # 1~45 번호까지 리스트 생성
print(lotto)

# 번호 45개 중에서 무작위 6개 뽑아오기
nums= random.sample(lotto, 6)
print(nums)
print()

# 낮은 번호 순으로 정렬
nums.sort()
print(nums)
print()
#-------------------------------------------------------------

#3. os 모듈 : 운영체제와 관련된 기능 모듈
import os 

print('현재의 운영체제: ', os.name)  #nt: windows   posix: mac or linux
print('현재 작업폴더: ', os.getcwd() ) #current working directory
print('현재 디렉토리(폴더)안의 있는 파일과 폴더목록들: ', os.listdir() )

#폴더 만들기
#os.mkdir('image') #만약. 이미 존재하는 폴더라면. 만들수 없음. 에러!!
print( os.path.isdir('image') )
if not os.path.isdir('image'):
    os.mkdir('image')
    
# 폴더 삭제
if os.path.isdir('image'):
    os.rmdir('image')     # rmdir: remove directory

# # 파일 이름 변경 --- 새로운 파일을 만들고 이름을 변경해 보기.
with open('nice.txt', 'w', encoding='utf-8') as file:
    file.write('Hello Phthon....')

# os.rename('nice.txt', 'good.txt') #변경하려는 파일명이 있는지 확인
if os.path.exists('good.txt'):
   #원래는 변경못하도록.. 해야 하지만.. 지금은 연습으로.. 그 파일을 제거하고.. 이름을 변경
   os.remove('good.txt')
   os.rename('nice.txt', 'good.txt')
print()

# 명령 프롬프트(터미널)에서 실행했던 명령어를 코드로 실행할 수도 있음. system()
os.system('dir')
os.system('python ex01_print.py')

# change directory 명령은 일부 안됨.
os.system('cd..') #안됨. change directory 전용함수를 이용해야 함.

print( os.getcwd() )
os.chdir('..')
print( os.getcwd() )
print()

#4. datetime 모듈: 날짜와 시간 관련 기능 모듈
import datetime

#현재 날짜와 시간을 얻어오기.
now= datetime.datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

# 원하는 날짜로 변경 가능
future= now.replace(year=(now.year+1))   # 원본 now는 불변(안 바뀐다)
print(future)
print(now)
print()

# 시간대 용어
# GMT 시간  >> 그리니치 천물대 기준 시간.. 경도 0 (런던시간대). 한국 GMT+0900
# UTC 시간  >> GMT를 기반으로 하되 지역별 시간대와 상관없이 1970년 1월 1일 자정(0시0분0초)를 기준으로 밀리초마다 카운트한 원자시간 값.세계협정시간
# UTC의 밀리초 카운트값이 가장 정확한. 경과시간을 계산할 수 있어서.. 컴퓨터공학 같은 곳에서 사용하는 시간...

# 그 밀리초의 카운트값을 확인할 수 있음. 이를 타임스탬프 라고 부름.
print( now.timestamp() )
print()

# # 특정 작업의 경과시간을 계산할때 활용
# start_time= datetime.date
# for n in range(10000):
#     print()

# elispsed_time= datetime.datetime_CAPI.now() - start_time  #타임스탬프의 차이값
# print('반복작업의 경과시간: ', elispsed_time)
# # datetime 객체는 보유 시간의 차이를 - 연산자로 알아서 잘 계산해 줌

a_day= datetime.datetime(2025,11,10) #교육시작일
today= datetime.datetime.now() #오늘
print('개강일로부터 : ', today- a_day)
print()

b_day= datetime.datetime(2026, 4, 9) #교육종료일
print('수료일까지 남은 날짜: ', b_day - today)
print('수료일까지 남은 날짜: ', (b_day - today).days, "일" )
print()

#5. time 모듈
import time
#현재 시간의 타임스탬프로 경과시간 계산식!!

aa= datetime.datetime.now().timestamp()
while True:
    if datetime.datetime.now().timestamp() - aa > 3 : 
        break
    print('.', end='')
    
print('3초간 프로그램을 잠시 정지했다가.. 다음 코드가 실행하도록')
time.sleep(3) #3초간 자다가 알아서 일어나서 다음코드로 진헹.
print('hello PYTHON')
print("-"*20)
print()
#---------------------------
#6. urllib 모듈 : 네트워크를 통해 서버의 데이터를 가져오는 모듈
# from urllib import request

# url= request.urlopen('https://www.naver.com')
# url= request.urlopen('https://n.news.naver.com/article/437/0000466369?cds=news_media_pc&type=editn')
# data= url.read()
# print(data.decode('utf-8'))
# print()

