# 파일 처리(입출력)을 위한 파이썬의 표준 내장함수가 있다.

#1. 파일에 데이터를 저장하기 - 파일명을 경로 없이 쓰면 이 .py파일이 있는 곳과 같은 위치에 만들어짐(이미 그 파일명이 있으면 덮어쓰기, 없으면 파일생성)
file = open("aaa.txt", "w", encoding='UTF-8')  #mode : 'w', write, 'a' append, 'r' read, #한글을 출력하려면 'URF -8'을 입력해줘야 함

file.write("This is Python Programming...! \n한글도 출력 될까?? ")

file.close()
#파일쓰기 작업이 종료되면 반드시.. 스트림을 닫아야 한다. 아니면 리소스 낭비가 된다.
#-------------------------------------------------------------------------
#2. 파일에서 텍스트 데이터 읽어오기...
file= open('aaa.txt', 'r', encoding='UTF-8') #파일명이 없으면... 못 읽어오기에 만들어주지 않고,.. 안 읽어짐.

contents= file.read()
print('파일에서 읽을 텍스트: ', contents)

file.close()
print()

#3. 파일 이어쓰기... append mode
file= open('bbb.txt', 'a', encoding='UTF-8')

file.write('apple')
file.write('banana')
file.write('orange')

file.close()

file= open('ccc.txt', 'a', encoding='UTF-8')

file.write('apple\n') #줄바꿈 기호는 글씨이다. 따옴표 안에 위치해야 함
file.write('banana\n')
file.write('orange\n')
file.close()

#(응용) 사용자로부터 한줄 리뷰를 계속 입력받아.. 파일에 저장. 단, 'quit'을 입력하몀ㄴ 입력을 종료하는 프로그램
file= open('ddd.txt', 'a', encoding='UTF-8')

while True:
    message= input('리뷰 입력: ')
    if message=='quit' or message=='그만':
        break

    file.write(message +'\n')
file.close()
#-------------------------------------------------
#4. 파일경로에 폴더명....
file= open('files/aaa.txt', 'w')  
#files 폴더안에 파일을 만듦.. [만약. files라는 폴더가 없다면..에러!! 폴더(디렉토리)는 자동으로 만둘어주지 않음]
file.write('Nice to meet you')
file.close()
# files 폴더를 사용자PC에 직접 만들면 되지만.. 실제 이 프로그램이 실행되는 환경은 개발자 PC가 아니라. 사용자 PC임
# 그래서 파이썬에서 시스템의 폴더를 만들거나 삭제할 수있음. 이를 위한 별도의 라이브러리(모듈)가 존재함. OS라는 이름의 모듈
# 경로를 지절할때. 상대경로..(상위폴더를 지칭하는 경로)
file= open('../aaa.txt', 'w')   # ..은 상위폴더를 지칭하는 경로
file.write('Have a goood day~~!!')
file.close()

# 경로를 모두 현재 위치를 기준으로 한 경로만 해 봤음.. 이런 경로를 상대경로 라고 부름.
# 특정 경로를 풀네임으로 지정할 수도 있음... 절대경로 라고 부름.

# file= open('C:\\aaa.txt', 'w') #Permission denied: 'C:\\aaa.txt'
file= open('C:\\users\\Admin\\aaa.txt', 'w')
file.write('aaaa')
file.close()

# 경로에 대한 학습은 추후에 배울 모듈 수업에서 다시 설명 및 소개


#5. 문자열 중에.. 여러 문자열 ''' ''' 이것도 당연히 한번에 쓰기 가능함.
file= open('files/bbb.txt', 'w')
data=''' \    # 역슬래시 사용으로 첫번째 한줄을 띄우지 않게 할 수 있다.
안녕하세요.
여러줄의 데이터를 써 봄니다.
줄바꿈이 될까요?
this is multiple line message.
'''
file.write(data)
file.close()
#--------------------------------------------------
#6. 
# 리스트데이터들을 저장해보기...
# names= [ '강중구', '김종경', '유지희', '최준영' ] 
# print(names)
# # 데이터를 원하는 형태로 전처리하는 것.
# new_names= map( lambda s:s+'\n', names)
# new_names= list(new_names)
# print(new_names)

# file= open('files/902호 학생들.txt', 'w', encoding='UTF-8')
# #file.write(names) #error
# file.writelines(new_names)  #줄바꿈을 자동으로 해 주지 않음 [해결은 원본 데이터들에 줄바꿈 문자를 추가해서 저장]
# file.close()
# print()
#-------------------------------------------------------
#7. 파일 다룰때 주의할점.. close()를 잊지 않아야 함. 개발자도 사람이라 실수의 여지가 있다
# 이를 보완하는 특별한 키워드 등장.with 키워드

# with open('ggg.txt', 'w') as file:
#     file.write('Hello Python')
# #close()를 안 해도 자동으로 with 영역이 종료되면 file 객체에게 close()를 요청해 줌.

# #8. 아주 긴 파일을 읽어와서 출력해 보기  
# # with open('files/long story.txt', 'r', encoding='UTF-16') as file:  # 'cp949(ANSI)', 'UTF-8', 'utf-16', ECU- 
# #     contents= file.read() # 모든 글씨를 하나의 문자열로 읽어오기
# #     print(contents)
# # print("-"*20)

# #9. 대량의 데이터를 파일로 부터 읽어서 분석하려면.. 일단. 대부분의 경우 한줄 단위로 처리함.
# # 그러려면.. split('\n')을 통해 한줄 단위로 분리하여 리스트로 만들어 처리..
# # 이 작업이 번거로워서.. 다행히 file 객체가 이미 한줄 단위씩 읽어오는 기능함수가 존재함.

# with open('files/short story.txt', 'r', encoding='utf-8') as file:
#     line= file.readline() # 한줄 읽기
#     print('첫번째 줄 문자열: ', line)
# print("-"*20)
# print()

#10. 
# 데이터분석을 하려면 데이터셋(data set)파일들을 많이 읽어와야 하는데... 보통 이 파일들은 엑셀형태가 많음.
# 엑셀파일을 읽어서 데이터를 분석하는 경우가 아주 많음.. 이를 시도... 했으나 
# 엑셀이나. hwp 파일들은 데이터외 추가정보를 보유하고 있어서 그래도 읽어지지 않음.
# 파이썬의 표준 함수 중에는 엑셀파일을 읽을 수 있는 기능함수가 없음.
# 외부 라이브러리 중에는 존재 함... 보통 이를 사용함. pandas 라이브러리에..엑셀 파일 쉽게 읽어오는 기능 존재 함.

# 대부분의 분석할 데이터들을 표(행: row, 열: column)형태를 가지고 만들어짐.
# 이를 위해 등장한 데이터표기형식(csv, xml, json)
with open('files/member.csv', 'r', encoding='utf-8') as file:
    # contents= file.read() # 통으로 한번에 모두 읽어오면 분석할때 짜증남.
    # 보통의 표형태의 데이터 구조는 한줄에 한 아이템의 정보들이 존재함.
    # 그래서 한줄 단위로 읽어서 처리함
    for line in file:    # 자동으로 readline()을 하면서 반복수행함.
        print('한줄 데이터: ', line)

    # 1줄 안에 있는 여러개의 데이터를 분리해서 취득하기 - csv 분석(parse)
    # data_list = line.split(',')
    # print(data_list)
    # print('이름 :', data_list[0])
    # print('나이: ', data_list[1])
    # print('주소: ', data_list[2])

    # 인덱스 번호로 칸의 의미를 해석하기 불편 -- 리스트의 요소를 분해하여 변수에 대입
    # name, age, address=data_list
    # print('이름 : ', name)
    # print('나이: ', age)
    # print('주소: ', address)
        name, age, address= line.split(',')
        print('이름: ', name)
        # 나이를 1 증가시킨 값을 출력하고 싶다면...
        if age.strip().isdigit(): #문자열이 숫자로만 이루어졌는가?
            print('나이: ', int(age)+1)
        print('주소: ', address)

#     name, age, address= line.split(',')
#     print('이름 : ', name)
#     print('나이: ', age)
#     print('주소: ', address)
# print('주소: ', address)

#[추가] mode 지정할때 + 기호

#1) w+ (읽기+쓰기 모두 가능 - '완전 덮어쓰기'...기존데이타를 모두 지우고 작성)
with open('files/ggg.txt', 'w+',encoding='utf-8') as file:
    file.write('new data.......') #파일커서의 위치가 글씨의 마지막에 있어서 그냥 읽으면..이후 데이터 없음.
    file.seek(0) #커서를 처음 위치로....
    contents= file.read()
    print(contents)

#2) a+ (읽기쓰기 가능, 이어붙이기!!) 
with open('files/ggg.txt', 'a+', encoding='utf-8') as file:
    file.write('새로운 데이터.....')
    file.seek(0)
    print(file.read())

#3) r+   (읽기+쓰기 ~ 덮어쓰기,,, 단, w+ 와 다르게 전체를 지우고 쓰지 않아요. 그냥 처음부터 덮어서 써버림)
with open('files/ggg.txt', 'r+', encoding='utf-8') as file:
    file.write('덮어쓰기')
    