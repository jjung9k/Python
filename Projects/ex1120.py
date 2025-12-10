# for 반복문과 범위
for n in range(5):
    print(str(n) + "=반복변수")
print()

for n in range(5, 10):
    print(str(n) + "=반복변수")
print()

for n in range(0, 10, 3):
    print(str(n) + "=반복변수")
print()

# 리스트와 범위를 조합해서 사용하기
array = [273, 32, 103, 57, 52 ]
for n in range(len(array)):
    print("{}번째 반복: {} ".format(n, array[n]))
print()

# 반대로 반복하기(1)
for n in range(4, 0, -1):
    print("현재 반복 변수: {}".format(n))
print()

#반대로 반복하기(2)
for n in reversed(range(5)):
    print("현재 반복 변수: {}".format(n))
print()

# 반복문으로 피라미드 만들기(1)
output = ""

for n in range(1, 10):
    for j in range(0, n):
        output += "*"
    output += "\n"
print(output)

output = ""
for n in range(1, 15):
    for j in range(14, n, -1):
        output +=' '
    for k in range(0, 2*n-1):
        output +='*'
    output += '\n'
print(output)
print()
# while 반복문을 for 반복문처럼 사용하기
n = 0
while n < 10:
    print("{}번째 반복입니다.".format(n))
    n +=1
print()

#해당하는 값 모두 제거하기
# test = [1, 2, 1, 2]
# value = 2

# while value in test:
#     test.remove(value)
# print(test)
# print()

# # 5초 동안 반복하기
# import time
# number = 0
# target_tick = time.time() + 5  #time.time() 은 현재 시간을 숫자로 보여주는 함수 임
    
# while time.time() < target_tick:
#     number += 1

# print("5초동안 {}번 반복 했습니다.".format(number))
# print()
#----------------------------------

# n = 0
# while True:
#     print("{}번째 반복문이니다.".format(n))
#     n += 1
#     input_text = input("> 종료하시겠습니까?(y/n): ")
#     if input_text in ["y", "Y"]:
#         print("반복을 종료합니다.")
#         break
# print()

# 범위는 정수의 범위를 나타내는 값입니다. range() 함수로 생성합니다.
# while 반복문은 조건식을 기반으로 특정코드를 반복해서 실행할 때 사용하는 구문입니다.
# break 키워드는 반복문을 벗어날때 사용하는 구문 입니다.

key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", 200, 30, 5]
chr ={}   # 여기는 비어 있는 캐릭터 정보 상자(딕셔너리)를 만드는거야.

for i in range(0, len(key_list)):
    chr[key_list[i]] = value_list[i]

print(chr)
# 라벨 리스트 + 값 리스트 >> 캐릭터 정보 만들기
print()

# 1부터 숫자를 하나씩 증가시키면서 더하는 경우를 생각해 보자. 몇을 더할때 1000을 넘는지 구해 보자. 그리고 그때의 값도 출력해 보자. 
limit = 10000
i = 1
sum_v = 0
while sum_v < limit: 
    sum_v += i
    i += 1 
print("{}를 더할때 {}를 넘으면 그때의 값은 {}입니다.".format(i, limit, sum_v))
print()

# 1부터 100까지의 숫자가 있다고 하자. 이를 다음과 같이 계산한다고 했을때, 최대가 되는 경우는 어떤 숫자를 곱했을 때인지를 찾아 줘.
max_v = 0
a = 0
b = 0

for n in range(1, 100 // 2 + 1):
    j =100 - n
    current = n * j
    if max_v < current:
        a = n
        b = j
        max_v = current
print("최대가 되는 경우: {} * {} = {}".format(a, b, max_v))
print()

# 소수점 아래 자릿수 지정하기
a = "{:15.3f}".format(52.273)
b = "{:15.2f}".format(52.273)
c = "{:15.1f}".format(52.273)
print(a)
print(b)
print(c)
