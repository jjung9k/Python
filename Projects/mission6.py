# 문제5) 사용자로부터 입력 받은 정수의 평균을 출력하는 프로그램을 작성. 두가지 조건을 만족해야 한다.
# 1.먼저 몇개의 정수를 입력할것인지 사용자에게 묻는다. 그리고, 만들어진 수만큼 정수를 입력 받는다.
# 2.평균값은 소수점 이하까지 출력되도록 한다.
# count= int(input("# 몇개의 정수를 입력하시겠습니까? "))
# total = 0 
# for i in range(count):
#     num= int(input("- 정수를 입력하세요: "))
#     total += num      #입력 된 정수를 토탈에게 계속 더함
# average = total/count #평균 계산
# print("평균은 {:.2f} 입니다.".format(average))  #소수점 둘째자리까지 출력
# print()

# 문제4) 사용자로부터 입력받은 숫자에 해당하는 구구단을 차례로 출력하고, 역순으로 출력하는 2개의 프로그램을 작성해 보시오.
# n = int(input("출력하고 싶은 구구단 단수를 입력하세요: "))
# for i in range(1, 10, +1):
#     print(n, 'x', i, '=', n * i)
# print()

# r = int(input("출력하고 싶은 구구단 단수를 입력하세요: "))
# for i in range(9, 0, -1):
#     print(r, 'x', i, '=', r * i)
# print()

# 람다 손코딩
power = lambda x: x * x  # 람다 X: 곱셈 >> 결과: [1, 4, 9, 16, 25]
under_1 = lambda x: x < 3  # 람다 X: 3보다 작은 수 >> 결과: [1, 2] 

a= [1,2,3,4,5]

output_a= map(power, a)
print("#map() 함수의 실행 결과")
print("map(power, a): ", output_a)
print("map(power, a): ", list(output_a))
print()

output_b = filter(under_1, a)
print("filter() 함수의 실행결과")
print("filter(under_3, a):  ", output_b)
print("filter(under_3, a):  ", list(output_b))
print()
# 339 page 손코딩 
# books= [{
#     "제목 : "혼자 공부하는 파이썬",
#     "가격 : 18900"},

# }]
# print()

# 과제) 함수 과제
kor = [92, 76, 88, 86] 
eng = [94, 80, 88, 90]
math = [95, 72, 81, 88]

def print_stats(subject, scores):
    avg= sum(scores) / len(scores)  # 평균 계산
    max_score= max(scores)
    min_score= min(scores)
    print(f"{subject} - 평균: {avg:.1f}, 최고점: {max_score}, 최저점: {min_score}")   #소수점 1자리까지 출력(.1f)

print("[과목별 통계]")
print_stats("국어", kor)
print_stats("영어", eng)
print_stats("수학", math)
print()

scores = {                 #딕셔너리 활용(과목별 점수 데이타)
    "국어": [92, 76, 88, 86],   # 콤마를 꼭 입력하고 구분해야 함. 리스트로 나눠야 하니..
    "영어": [94, 80, 88, 90],
    "수학": [95, 72, 81, 88]
}
print("<과목별 통계>")

for subject, score_list in scores.items():
    avg_score = sum(score_list) / len(score_list)
    max_score = max(score_list)
    min_score = min(score_list)

    print(f"{subject} - 평균: {avg_score:.2f}, 최고점: {max_score}, 최저점:{min_score}")
print()

def cel_to_fah(cel):     #섭씨를 화씨로 변환하는 함수
    fah = 1.8 * cel + 32
    return fah
def fah_to_cel(fah):     #화씨를 섭씨로 변환하는 함수( 공식: cel = (fah-32)/1.8  )
    cel=(fah - 32) / 1.8
    return cel

c = float(input("섭씨 온도를 입력하세요: "))
print("화씨 온도: ", cel_to_fah(c))

f = float(input("화씨 온도를 입력하세요: "))
print("섭씨 온도: ", fah_to_cel(f))
print()

def gugudan_range(a, b):
    start = min(a, b)
    end = max(a, b)

    print("========================================")
    print(" ◈ 구구단 출력 프로그램 ◈ ")
    print("========================================")

    for dan in range(start, end + 1 ):
        print(f" {dan}단 ")
        for i in range(1, 10):
            print(f"{dan} x {i} = {dan * i}")
        print("-------------------------------------")

    print("♥ 출력 완료 ♥")
    print("========================================\n")

num1= int(input("첫번째 숫자를 입력하세요: "))
num2= int(input("두번째 숫ㅈ를 입력하세요: "))
#함수 호출
gugudan_range(num1, num2)

aa= [10, 20, 30]

print(*aa)