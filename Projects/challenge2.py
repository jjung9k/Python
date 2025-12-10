#1. 도전문제 (구의 부피와 겉넚이 구하기)

pi = 3.141592
r= float(input('>> 구의 반지름을 입력해 주세요: '))
부피= (4/3) * pi * (r**3)   # 공식은 문제에 주어짐
겉넓이= 4 * pi * r**2       #  공식은 문제에 주어짐  
print(f"1. 구의 부피는 {부피} 입니다.")
print(f"2. 구의 겉넓이는 {겉넓이} 입니다.")
print()

#2. 피타고라스의 정리

밑변= float(input("밑변의 길이를 입력해 주세요: "))
높이= float(input("높이의 길이를 입력해 주세요: "))

빗변= (밑변**2 + 높이**2) ** (1/2)
print(f"= 빗변의 길이는 {빗변} 입니다.")
print()

# 요소 추가 하기
dictionary = {}
dictionary['name']= "새로운 이름"
dictionary['head']= "새로운 정신"
dictionary['body']= "새로운 몸"
print("요소 추가", dictionary)
print()

#랜덤하게 1000명의 키와 몸무게 만들기
import random
hanguls = list("가나다라마바사아자차카타파하")
with open("info.txt", "w", encoding='ANSI') as file:
    for i in range(1000):
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)

        file.write("{}, {}, {}\n".format(name, weight, height))

#반복문으로 파일 한줄씩 읽기 
with open("info.txt", "r") as file:
    for line in file:
        (name, weight, height)= line.strip().split(", ")
        #데이터가 문제가 없는지 확인합니다. 문제가 있으면 지나감 
        if (not name) or (not weight) or (not height):
            continue

        bmi= int(weight) / ((int(height) / 100) **2 )
        result = ""
        if 25 <= bmi:
            result = "과체중"
        elif 18.5 <= bmi:
            result = "정상 체중"
        else:
            result = "저체중"

        print('\n'.join([
            "이름: {}",
            "몸무게: {}",
            "키: {}", 
            "BMI: {}",
            "결과: {}"
        ]).format(name, weight, height, bmi, result))
        print()





