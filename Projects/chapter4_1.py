# 리스트 연산하기: 연결(+), 반복(*), len()
# list_a= [1,2,3]
# list_b= [4,5,6,7]

# print("# 리스트")
# print('list_a = ', list_a)
# print('list_b = ', list_b)
# print()

# print('# 리스트 기본 연산자')
# print('list_a + list_b= ', list_a + list_b)
# print('list_a * 3', list_a * 3)
# print()

# print("# 길이 구하기")
# print('len(list_a) = ', len(list_a))
# print('len(list_b) = ', len(list_b))
# print()

# # 리스트에 요소 추가하기: append(), insert()
# list_a = [1, 2, 3]

# print('# 리스트 뒤에 요소 추가하기')
# list_a.append(4)
# list_a.append(5)
# print(list_a)
# print()

# print('# 리스트 중간에 요소 추가하기')
# list_a.insert(0, 10) # 삽입할 위치가 0, 삽입할 값은 10, 이때 해당 위치의 요소는 뒤로 하나씩 밀려 [10,1,2,3,4,5]가 된다
# print(list_a)
# print()

# 리스트의 요소 하나 제거하기
list_a= [0,1,2,3,4,5]
print("# 리스트의 요소 하나 제거하기")

del list_a[1] 
print('del list_a[1]: ', list_a)

list_a.pop(2)
print('pop(2): ', list_a)
print()

# 리스트에 [ : ] 연산자로 리스트 범위를 지정하여 여러 요소를 선택하는 것을 슬라이싱이라 한다. 예) 리스트[시작_인덱스:끝_인덱스:단계]
# 반복문과 리스트
a = [273,32,103,57,52]
for element in a:
    print(element)
for cha in "안녕하세요.":
    print("--", cha, "--")
print()

# 중첩리스트와 중첩 반복문, 2차원 리스트에 반복문 2번 사용하기
list_of_list = [
    [1,2,3], [4,5,6,7], [8,9]
]
for items in list_of_list:
    for item in items:
        print(items)

# 딕셔너리는? key를 계산함... 즉... 원하는 값을 계산하지 않음.. 그러니 사용안함.
aaa={'a':20, 'b':40, 'c':30}
print(min(aaa))  # 알파벳(아스키) 순으로 우선순위 뽑는다.
print(max(aaa))
print()

list_a= [1,2,3,4,5]
list_reversed =reversed(list_a)

print("# resverse() 함수")
print("reversed([1,2,3,4,5]):", list_reversed)
print("list(reversed[(1,2,3,4,5)])):", list(list_reversed))
print()

print("# reversed() 함수와 반복문")
print("for i in reversed([1,2,3,4,5]): ")
for i in reversed(list_a):
    print("-", i)

ex_list= ["요소A", "요소B", "요소C"]

print("# 단순 출력")
print(ex_list)
print()

print("# enumerate() 함수 적용 출력")
print(enumerate(ex_list))
print()

print("# list() 함수로 강제 변환 출력")
print(list(enumerate(ex_list)))
print()

print("반복문과 조합하기")
for i, value in enumerate(ex_list):
    print("{}번째 요소는 {}입니다.".format(i, value))
print()

#딕셔너리의 items()함수와 반복문
# ex_dictionary = {
#      "키A": "값A",
#      "키B": "값B",
#      "키C": "값C",
#      }

# print("# 딕셔너리의 items() 함수")
# print("items(): ", ex_dictionary.items())
# print()

# print("# 딕셔너리의 items() 함수와 반복문 조합하기")

# for key, element in ex_dictionary.items():
#     print("dictionary[{}] = {}".format(key, element))
# print()
#반복문을 사용한 리스트 생성
# array= []

# for i in range(0, 20, 2):
#     array.append
    
# array = [ i * i for i in range(0, 20, 2)]
# print(array)
# print()

# # 조건을 활용한 리스트 내포 > 리스트  이름 = [표현식 for 반복자 in 반복할 수있는 것 if 조건문]
# array = [ "사과", "자두", "초코릿", "바나나", "체리"]
# output = [ aaa 
#           for aaa in array
#           if aaa != "초코릿"]
# print(output)
#if 조건문과 여러줄 문자열(1)
# number = int(input("정수 입력>  "))
# if number % 2 == 0:
#     print("""\
#           입력한 문자열은 {} 입니다.
#           {}은(는) 짝수입니다.""".format(number, number))
# else:
#     print("""\
#           입력한 문자열은 {} 입니다.
#           {}는(은) 홀수입니다.""".format(number, number))

# #if 조건문과 여러줄 문자열(2)
# number = int(input("정수 입력: "))
# if number %2 == 0:
#     print("""입력한 문자열은 {} 입니다.
#           {}는(은) 짝수입니다.""".format(number, number))
# else:
#     print("""입력한 문자열은 {} 입니다.
#           {}는 홀수입니다.""".format(number, number))
# print()
# if 조건문과 긴 문자열
# number = int(input("정수 입력: "))
# if number %2 == 0:
#     print("입력한 문자열은 {} 입니다. \n {}은 짝수입니다.".format(number, number))
# else:
#     print("입력한 문자열은 {} 입니다. \n {}은 홀수입니다.".format(number, number))
# print()

#딕셔너리 요소 추가하기.
# dictionary= {}

# print("요소 추가 이전: ", dictionary)

# dictionary["name"] = "새로운 이름"
# dictionary["head"] = "새로운 정신"
# dictionary["body"] = "새로운 몸"
# print("요소 추가 이후: ", dictionary)
# print()


# # 딕셔너리의 요소에 접근하기
# dictionary = { 
#     "name" : "7D 건조 망고",
#     "type" : "당절임",
#     "ingredient": ["망고", "설탕", "메타중아환산나트륨","치자황색소"],
#     "origin": "필리핀" 
# }
# print("1. name : ", dictionary["name"])
# print("2. type : ", dictionary["type"])
# print("3. ingredient : ", dictionary["ingredient"])
# print("4. origin : ", dictionary["origin"])
# print()
# #값을 변경한다.
# dictionary["name"] = "8D 건조 망고"
# print("name: ", dictionary["name"])
# print()

# dictionary = {
#     "name" : "7D 건조 망고",
#     "type" : "당절임"
#     }

# print("요소 제거 이전: ", dictionary)

# del dictionary["name"]
# del dictionary["type"]

# print("요소 제거 이후: ", dictionary)
# print()

#키가 존재하는지 확인하고 값에 접근하기.
# dictionary = {
#     "name": "7D 건조 망고",
#     "type": "당절임",
#     "ingredient": ["망고", "설탕", "메타중이황산", "치자황색소"],
#     "origin": "필리핀"
# }

# key = input(">접근하고자 하는 키: ")

# if key in dictionary:
#     print(dictionary[key])
# else:
#     print("존재하지 않는 키에 접근하고 있습니다.")
# print()

#키가 존재하지 않을때 None 을 출력하는지 확인하기.
# dictionary = {
#     "name": "7D 건조 망고",
#     "type": "당절임",
#     "ingredient": ["망고", "설탕", "메타중이황산", "치자황색소"],
#     "origin": "필리핀"
# }
# value = dictionary.get("존재하지 않는 키")
# print("값: ", value)

# if value == None: 
#     print("존재하지 않는 키에 접근했습니다.")
# print()

# dictionary = {
#     "name": "7D 건조 망고",
#     "type": "당절임",
#     "ingredient": ["망고", "설탕", "메타중이황산", "치자황색소"],
#     "origin": "필리핀"
# }

# for key in dictionary:
#     print(key, ":", dictionary[key])
# print()

#for 반복문과 범위
# for i in range(5):
#     print(str(i) + " = 반복 변수")
# print()

# for i in range(5, 10):
#     print(str(i) + " = 반복 변수")
# print()

# for i in range(0, 10, 3):
#     print(str(i) + " = 반복 변수")
# print()

#리스트와 범위를 조합해서 사용하기
# array = [273, 32, 103, 57, 52]

# for i in range(len(array)):
#     print("{}번째 반복: {}".format(i, array[i]))
# print()

# for i in range(10, 0-1, -1):  # 0 - 1, -1의 수식을 입력해야 함
#     print("현재 반복 변수: {}".format(i))
# print()

# for i in reversed(range(6)):
#     print("현재 반복 변수: {}".format(i))
# print()

# numbers = [5, 15, 6, 20, 7, 25]

# for number in numbers:
#     if number >= 10:
#         print(number)
# print()
#여러 줄 문자열과 if 구문을 조합했을 때의 문제해결(2)

# number = int(input("정수입력: "))
# if number % 2 == 0:
#     print("\n".join([
#         "입력한 문자열은 {} 입니다.",
#         "{}는(은) 짝수입니다."
#     ]).format(number, number))
# else:
#     print("\n".join([
#         "입력한 문자열은 {} 입니다.",
#         "{}는(은) 홀수 입니다."
#     ]).format(number, number))
# print()

# rebersed()함수와 이터레이터
numbers = [1,2,3,4,5]
r_num = reversed(numbers)

print("reversed_numbers : ", r_num)
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print()

# reversed() 함수는 매개변수에 리스트를 넣으면 요소의 순서를 뒤집을 수 있습니다.
# enumerate() 함수는 매개변수에 리스트를 넣으면 인덱스의 값을 쌍으로 사용해 반복문을 돌릴 수 있는 해 주는 함수이다.
# items()함수는 키와 쌍으로 사용해 반복문을 돌릴 수 있게 해주는 딕셔너리 함수입니다.

# output = [i for i in range(1, 100+1)
#     if "{:b}".format(i).count("0") ==1]

# for i in output:
#     print("{} : {}".format(i, "{:b}".format(i)))
# print("합계: ", sum(output))
# print()

#딕셔너리를 사용해서 숫자가 몇개 사용 되었는지 세고, len()함수를 사용해 세트에 키기 몇개 들어 있는지 확인
# a = [1, 2, 3, 4, 1, 2, 3, 1, 4, 1, 2, 3]
# counter = {}

# for i in a:
#     if i not in counter:
#         counter[i] = 0
#         counter[i] += 1
    
# print(f"{a} 에서")
# print(f"사용된 숫자의 종류는 총{len(counter)}개 입니다.")
# print()
# print(f">> 참고: {counter}")

# nuc = input("염기 서열을 입력해 주세요: ")
# counter = {
#     "a": 0,
#     "t": 0,
#     "g": 0,
#     "c": 0,
# }

# for nuc in nuc:
#     counter[nuc] +=1

# for key in counter:
#     print(f"{key}의 개수: {counter[key]}")
# print()

nuc = "ctacaatgtcagtataccattgcattagccgg"
for i in range(0, len(nuc), 3):
    codon = nuc[i:i+3]
if len(codon) == 3:
    print(codon)
print()



