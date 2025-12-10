#문제1) 학생들의 성적이 저장된 scores.csv 파일을 이용한 성적 통계 프로그램을 만들어보시오.
# 1. csv 파일 읽기: open() 함수를 사용하고 score.cvs 파일을 읽으시오.(첫줄을 제외한 나머지 줄의 점수를 숫자(int)데이터로 변환해야만 계산 가능)
# 2. 데이터 처리 : 각 과목(국어, 영어, 수학)에 대해 다음을 계산하시오.(평균, 최저점, 최저점)
# 3. 결과 출력: 각 과목별 통계 결과를 콘솔에 보기 좋게 출력하시오.
# 4. 각 학생의 총점과 평균도 계산하시오. 각 학생의 이름, 총점, 평균을 포함한 새로운 csv파일(result.csv)로 저장하시오.

file= open('./files/scores.csv', 'r', encoding='utf-8')

lines= file.readlines()     
file.close()

header= lines[0]
data = lines[1:] 

kor_scores= []
eng_scores= []
math_scores= []

students_result= []   # 이름, 총점, 평균 저장

for line in data:
    parts = line.strip().split(",")  # 각 열을 콤마 기준으로 분리시키고, 양옆 제거

    name= parts[0]
    kor= int(parts[1])
    eng= int(parts[2])
    math= int(parts[3])

    kor_scores.append(kor)
    eng_scores.append(eng)
    math_scores.append(math)

    total= kor + eng + math
    avg= total / 3
    students_result.append([name, total, avg])

def print_stats(subject, scores):
    avg= sum(scores) / len(scores)
    print(f"{subject} - 평균: {avg:.1f}, 최고점: {max(scores)}, 최저점: {min(scores)}")

print("[과목별 통계]")
print("-"*45)
print_stats("국어", kor_scores)
print_stats("영어", eng_scores)
print_stats("수학", math_scores)
print("-"*45)

output=open("result.csv", "w", encoding="utf-8")
output.write("이름, 총점, 평균\n")

for student in students_result:
    output.write(f"{student[0]}, {student[1]}, {student[2]:.1f}\n")

output.close()
print()
print("result.csv 저장완료!")

