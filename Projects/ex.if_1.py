# 과제3) 두수의 정수를 입력 받아 if~else의 한줄쓰기 문법인 삼항연산자를 이용하여 출력해 보시요. 삼항연산자
# a = int(input("첫번째 정수를 입력하세요: "))
# b = int(input("두번째 정수를 입력하세요: "))

# result = a - b if a > b else b - a

# print("두 수의 차이액: ", result)
# print()
# 과제4) 로그인 검사(미리 저장 된 ID와 패스워드를 기준으로 사용자가 입력한 값이 둘 다 일치하면 "로그인 성공")
# saved_id = "python"
# saved_pw = "1234"

# user_id = input("ID를 입력하세요: ")
# user_id = input("비밀번호를 입력하세요: ")
# if user_id == saved_id and user_pw == saved_pw:
#     print("로그인 성공")
# else:
#     print("로그인 실패")
# print()

#페이지 136~137 format() 함수는 {} 중괄호가 몇개인지에 따라 format () 갯수가 동일하게 입력되어야 함
format_a = "{} 만원".format(5000)
format_b = "파이썬 열공하여 첫 연봉 {} 만원 만들기".format(5000)
format_c = "{} {} {}".format(3000, 4000, 5000)
format_d = "{} {} {}".format(1, "문자열", True)

print(format_a)
print(format_b)
print(format_c)
print(format_d)
print()

# 정수를 특정 칸에 출력하기.
a = "{:d}".format(52)
b = "{:5d}".format(52)   # 특정 칸에 출력하기(5번 띄우고, 숫자 출력)
c = "{:10d}".format(52)  # 특정 칸에 출력하기(10번 띄우고, 숫자 출력) 
d = "{:05d}".format(52)  # 빈칸을 '0'으로 채울때 사용 :05d
e = "{:05d}".format(-52) # 음수를 출력할때 사용
print(a)
print(b)
print(c)
print(d)
print(e)
print()

f = "{:d}".format(52)
g = "{:+d}".format(-52)
h = "{: d}".format(52)
i = "{: d}".format(-52)
print(f)
print(g)
print(h)
print(i)
print()

# 정수를 양수/음수 조합해 보기
j = "{:+5d}".format(52)
k = "{:+5d}".format(-52)
l = "{:=+5d}".format(52)
m = "{:=+5d}".format(-52)
n = "{:+05d}".format(52)
o = "{:+05d}".format(-52)
print(j)
print(k)
print(l)
print(m)
print(n)
print(o)
print()
