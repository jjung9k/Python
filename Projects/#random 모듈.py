#random 모듈
import random
print("# random 모듈")

print("- random(): ", random.random() )

print("- uniform(10, 20): ", random.uniform(10,20) )

print("- rangrange(10) : ", random.randrange(10) )

print("- choice([1,2,3,4,5])", random.choice([1,2,3,4,5]) )

print("- shuffle([1,2,3,4,5]): ", random.shuffle([1,2,3,4,5]) )

print("- sample([1,2,3,4,5]), k=2): ", random.sample([1,2,3,4,5], k=2) )
print()

list_a=[1,2,3]

list_a.append(4)
list_a.append(5)
print(list_a)
print()

list_a.insert(6, 10)
print(list_a)
print()

# list_a= [0,1,2,3,4,5]

# del list_a[2]     # 리스트의 2번째 요소값 제거(del 키워드 사용)
# print("리스트 요소 제거: ", list_a)

# array = [273, 32, 103, 57, 52]

# for i in array:
#     print(i)
# print()

# for ch in "안녕하세요":
#     print("#", ch)
# print()

#2차원 리스트에 반복문 한번 사용하기

# list_of_list = [
#     [1,2,3],[4,5,6,7],[8,9]
# ]

# for items in list_of_list:
#     print(items)
# print()

# #2차원 리스트에 반복문 두번 사용하기
# list_of_list = [
#     [1,2,3],[4,5,6,7],[8,9]
# ]
# for items in list_of_list:
#     for item in items:  # for문을 2번 돌려서 리스트의 요소를 두번씩 출력하기
#         print(items)
# print()

for i in range(5):
    print(str(i) + "=반복변수")
print()

for i in range(5, 10):
    print(str(i) + "=반복변수")
print()

for i in range(0, 10, 3):
    print(str(i) + "=반복변수")
print()

#리스트 범위를 조합해서 사용하기
array = [273, 32, 103, 57, 52]

for i in range(len(array)):
    print("{}번째 반복: {}".format(i, array[i]))
print()

for i in range(4, -1, -1):
    print("현재 반복 변수: {}".format(i))
print()

for i in reversed(range(5)):
    print("현재 반복 변수: {}".format(i))
print()

output =""

for i in range(1, 10):
    for j in range(i):
        output +="*"
    output += "\n"

print(output)

output2 =""
for i in range(10, 0, -1):
    for j in range(i):
        output2 += "#"
    output2 += "\n"
print(output2)
print()

n=5
for i in range(1, n+1):
    print(" " * (n-i) + "*" * (2 * i -1))

for i in range(n - 1, 0, -1):
    print(" " * (n-i) + "*" * (2 * i -1))
print()

m=5
for j in range(1, m+1):
    print(" " * (m-j) + "$" * (2 * j-1 ))

for j in range(n -1, 0, -1):
    print(" " * (m-j) + "$" * (2 * j-1))
print()
