# 문제1번.
# name = "강중구"
# age = 48
# hobby = "배드민턴"
# print("제 이름은 "+ name + "이고, 나이는 " + str(age) + "살 입니다.")
# print("제 취미는 " + hobby + "입니다.")
# print()
# print(f"제 이름은 {name}이고, 나이는 {age}살 입니다.")
# print(f"제 취미는 {hobby}입니다.")

# 문제2번. 자료형 확인하기 다음 변수를 만들고, 각각의 자료형을 출력해 보세요. type() 함수는 변수의 자료형을 확인할 때 사용하는 방법
# name = "강중구"   # 문자의 함수는 'str' 이다.
# age = 48         # 나이나 숫자의 함수는 정수 'int' 이다
# height = 179.3   # 무게, 중량 등은 함수는 'float' 이다
# is_student = True # 참이냐 거짓이냐 사용시 함수 'bool' 이다

# print("name의 자료형: ", type(name))
# print("age의 자료형: ", type(age))
# print("height의 자료형: ", type(height))
# print("is_student의 자료형: ", type(is_student))
# print()

# 문제3번. 간단한 계산기 만들기. 각각의 변수를 저장한 뒤 덧셈, 뺄쎔, 곱셈, 나눗셈 결과를 각각 출력해 보세요. 
# a = 10
# b = 3
# add = a + b
# print("덧셈 결괴: ", add)
# sub = a - b
# print("뺄셈 결과: ", sub)
# mul = a * b
# print("곱셈 결과: ", mul)
# div = a // b    # 소수점을 없애고 싶을 때는 // (슬래시 2개) 로 입력!!
# print("나눗셈 결과: ", div)

# 문제4번. 변수 활용 문장 완성하기  # 변수 예시 아래 3개 보기
# country = "한국"
# city = "서울"
# year = 2025
# print("저는 " + str(year) + "년도에" + " " + country + "의 수도~" + " " + city + "에 살고 있습니다.")
# print()

# 문제5번. 프로그램 사용자로부터 두개의 정수를 입력 받아서 두 수의 뺄셈 과 곱셈, 나눗셈의 결과를 출력하는 프로그램을 작성.
# a = int(input("첫번째 정수를 입력하세요: "))
# b = int(input("두번째 정수를 입력하세요: "))
# sub = a - b
# print("뺄셈 결과: ", sub)
# mul = a * b
# print("곱셈 결과: ", mul)
# div = a // b 
# print("나눗셈 결과: ", div)
# print()

# 문제6번. 프로그램 사용자로부터 세 개의 정수 num1, num2, num3를 순서대로 입력 받은 후에, 다음 연산의 결과를 출력하는 프로그램을 작성해 보세요(입력문은 세번 사용)
# num1*num2+num3 단, 입력 받은 세 개의 정수가 2,4,6 이라면 다음의 형태로 출력을 해야 한다. 예시 2*4+6=14
# num1 = int(input("첫번째 정수를 입력하세요: "))
# num2 = int(input("두번째 정수를 입력하세요: "))
# num3 = int(input("세번째 정수를 입력하세요: "))

# re = num1 * num2 + num3
# print("결과값:", f"{num1}*{num2}+{num3}={re}")
# print()

# 문제7번. 프로그램 사용자로부터 두 개의 실수를 입력 받아서 2개의 변수를 저장하자. 그리고 두 변수의 사칙연산 결과를 출력해보자
# a = float(input("첫번째 실수를 입력하세요: "))
# b = float(input("두번째 실수를 입력하세요: "))
# add = a + b
# sub = a - b
# mul = a * b
# div = a / b
# print("덧셈 결과값: ", add )
# print("뺄셈 결과값: ", sub )
# print("곱셉 결과값: ", mul )
# print("나눗셈 결과값: ", div )
# print()

# 문제8번. 마일을 킬로미터로 변환하는 프로그램을 작성하자. 1마일은 1.609킬로미터와 같다. 실행되는 입출력의 모양은 아래와 같이 만들어보자. [예시의 입력값 10은 사용자의 입력값 임]
mile = float(input("마일을 입력하세요: "))
km = mile * 1.609
print(f"{mile} 마일은 {km} 킬로미터입니다.")

