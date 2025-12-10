# 프로그램에서 사용하는 대부분의 데이터는 문자열인 경우가 많음.
# 문자열의 연산자와 기능함수들...

# 문자열 연산자 3개
#1) + 결합연산자
print("aaa"+"bbb")
#2) * 반복 연산자
print("nice"*5)
s= "Hello world"
print( s[2] ) #2번 인덱스 위치의 문자 1개를 취득(3번째 글자)
print( s[2:8]) #2~8번 전까지(2~7)
print( s[2:]) #2~ 끝까지
print( s[:5]) #시작~4번까지
print( s[-2]) #뒤에서 2번 위치...
print()

#문자열의 길이(length)[글자수]를 알려주는 파이썬의 내장함수
a= len(s)
print('글자수: ', a)
print()

print( "Hello".upper()) #대문자로 변경
print( "Hello".lower()) #소문자로 변경

word= 'Machine Learning'
print(word.upper())
print(word.lower())
#[중요!] 기능을 사용하더라도 원본 문자열을 변경되지 않음
s= word.upper()
print( word )
print( s )
print()

#3) .strip() : 문자열의 양옆의 공백만 제거하는 기능함수
word= '  Hello  '
print("[", word, "]")
print("[", word.strip(), "]")
#검색어 비교..  또는 아이디 비교 작업할때 필수로 공백제거 후 비교함
print( word == 'Hello' )  #False
print( word.strip() == 'Hello' ) 

#4)  .find(): 특정 문자의 인덱스 번호 위치를 찾아주기
s = 'Hello world. android. ios. ai. world'
print( s.find('world')) #찾은 글씨의 첫번째 글자 인덱스 번호
print( s.find('ANDROID')) #대소문자는 다른 글자임. [못찾으면 -1로 표기] 음수로 표기 된다.
# 혹시 같은 문자가 여러개면.. 앞에서부터 검색하기에 앞에 문자(번호)부터 먼저 찾고 기능 멈춤.
# 만약 뒤에 있는 문자도 찾으려면... 추가 find
idx= s.find('world') #6
print( s.find('world', idx+1)) #앞에 찾은 글씨 인덱스번호 다음부터 다시 찾아라.
print()

#5) in 연산자 [ 기능함수 아님.. () 없음]  --- 특정문자가 그 문자열안에 있는지 여부(True/False)를 알려주는 연산자
print("world" in s ) # s 라는 변수가 가진 문자열에 'wordl'라는 글씨가 있나요? True
print( "WORLD" in s)
#대소문자 구분없이 특정 문자의 존재여부를 알고 싶다면....
print( "WORLD" in s.upper()) # upper를 활용해서 대문자로 바꿔서 나오게 한다. True

#6) replace - 글자 바꿔치기 
s = 'Hello world.nice world. good world'
# world 글자들을 python 이라는 글씨로 변경해서 출력.
print(s.replace('world','python'))
# 기능을 사용해도 원본은 불변!
print( s )
# 대소문자는 다른 것이라고 생각함.
print(s.replace('WorLD','coding')) #바꿀 글씨가 없으면..
# 만약 대소문자 상관없이 찾아서 바꾸고 싶다면... 아래 예시
print( s.replace('WorLD'.lower(), 'coding'))
aa= s.replace(" ", "")
print(aa)
s= s.replace("\n", "")
# 비속어 걸러내기..
s= s.replace("Fuxx", "^^")
s= s.replace("개XX", "^^")
print()

#7) .split() : 특정 문자를 기준으로 글씨를 나누어서 [리스트: 여러데이터를 한번에 가지는 변수]로 만들어 주는 기능함수
aaa= [10, 20, 30, 40]
print(aaa)
print(aaa[0])
print(aaa[1])
csv= 'sam,20,seoul'  #콤마로 구분한 값을 각각 나누어 주는 것
aaa= csv.split(',')
print(aaa)
print(aaa[0])
print(aaa[1])
print(aaa[2])
print()

#8) isXXX() 기능함수들...
#8.1] 알파벳으로만 이루어져 있는가?
print( "Hello".isalpha() )     #True
print( "Hello123".isalpha() )  #False
print( "Hello안녕하세요".isalpha()) #True

#8.2] 숫자로만 이루어 졌나요? (숫자, 로마숫자, 윗첨자)
print( "1234".isnumeric() )
print( "1234abc".isnumeric() )
#int() 형변환이 가능하지를 알수 있음.
print( "3.141592".isnumeric())  #False  . 소수점은 특수문자
print(  "300     ".isnumeric())  #False
print(  "300  ".strip().isnumeric()) #True
print("Ⅳ".isnumeric()) #로마 숫자
print("4²".isnumeric()) #윗첨자 숫자
#8.3] 로마자는 제외한 숫자만 허용 [아라비아숫자 + 윗첨자]
print( "1234".isdigit())
print( "1234abc".isdigit())
print( "Ⅳ".isdigit())
print( "4²".isdigit())
print()

#8.4] 오직 아라비아 숫자만 허용



#8.5] 알파벳과 숫자로만 이루어져 있는가? (특수문자 제외) 


#8.6] 모두 소문자인가?
print( "Hello world".islower())
print( "hello wolrd".islower())
print()

#9) count() : 문자열 안에 특정 단어가 몇개인지 알려주는 기능함수
message= "EDA(Exploratory Data Analysis) : 탐색적 데이터 분석. data를 다양한 각도에서 관찰하고 이해하는 첫번째 단계. 시각화와 통계적 기법을 사용하여 Data를 분석 합니다"
print( 'data라는 문자의 개수:', message.count('data') )
print( 'data라는 문자의 개수:', message.lower().count('data') )