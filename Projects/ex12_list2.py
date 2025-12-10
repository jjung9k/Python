# 리스트를 생성하는 특별한 문법 [리스트 내포 list comprehensions]
# 반복문으로 리스트의 요소를 만들때 한 줄로 간결하게 만들 수 있는 문법

#1] 기존 방식대로 반복문으로 리스트 생성
# aaa = [] #비어 있는 배열
# for n in range(1,10):   #1부터 9까지 범위지정
#     aaa.append(n)       #추가하기 위한 문법 append 

# print(aaa)

# bbb= [ n for n in range(1,10)]
# print(bbb)

# ccc= [n * 10 for n in range(1,10)]
# print(ccc)

# ddd= [n ** 2 for n in range(1,10)]
# print(ddd)

# 추가...문법) 기존 리스트의 값 중 특정조건을 통과한값으로만 새로운 리스트를 만들 수 있음
# score= [70, 80, 95, 42, 68, 73, 57, 84]

#60점 미만을 걸러내고 새로운 리스트 생성
# eee=[]
# for score in scores:
#     if score>= 60:
#         eee.append(score)
# 
# eee= [score for score in scores if score>= 60 ] #실제 데이터분석이나 ML작업할때 필터링을 위해 자주 활용되는 문법
# print(eee)
# print()

# 사용자의 입력된 숫자만큼 빈 리스트의 요소를 만들기. 단, 리스트의 초기값은 0으로...
# num= int(input('개수: '))
# ggg= [0 for n in range(num)]
# print(ggg)

# 가장 손쉽게 순차적인 값을 가지는 리스트 생성하는 방법 - 리스트를 만들어

for v in [1,2,3,4]:
    print(v)
for v in range(1, 6):
    print(v)

hhh= [1,2,3,4,5]
print(hhh)

ggg= range(1, 6)
print(ggg)

kkk= list(range(1,6))
print(kkk)





# 리스트를 다루는 특별한 문법과 기능함수들....

#1-1] 리스트나 튜플의 요소들 중 최소값, 최대값, 합계를 구해주는 함수
score_list= [48, 100, 85, 72, 64, 23, 5, 18]

print('최소값 : ', min(score_list))
print('최대값 : ', max(score_list))
print('총합 : ', sum(score_list))
print('평균 : ', sum(score_list)/len(score_list))

# 딕셔너리는? key를 계산함... 즉... 원하는 값을 계산하지 않음.. 그러니 사용안함.
aaa={'a':20, 'b':40, 'c':30}
print(min(aaa))  # 알파벳(아스키) 순으로 우선순위 뽑는다.
print(max(aaa))
print()

#2] for 반복할때 인덱스번호와 값을 동시에 주는 함수
aaa= ['sam','robin', 'hong', 'park']
for val in aaa:
    print(val)
print()

for idx, val in enumerate(aaa):
    print(idx, ":", val)
print()

#3] 요소의 순서를 뒤바꾸는 함수 reversed() --- 원본리스트틑 변경되지 않고, 뒤바낀 새로운 배열을 리턴해 줌.
# ~마치 range() 같은.. 
aaa= [10, 20, 30, 40, 50]
bbb= reversed(aaa) #aaa리스트의 요소 위치를 바꾸어 새로운 리스트를 만들어주는 녀석을 줌
print(aaa)
print(bbb)
# range처럼 반복문을 사용하면.. 뒤바낀 요소를 줌
for v in bbb:
    print(v)
#for문 사용이 싫다면... 리스트로 만들기
ccc= list(reversed(aaa))
print(ccc)
# 혼동하기 쉬운 리스트의 기능함수...
aaa.reverse()  #리스트의 기능임. 이것은 원본 리스트의 순서가 바뀜 >> reversed 와는 다르다.
print(aaa)
print()

# python 3.0버전 이상에서 완전 도입 된 {set:집합} 자료형
aaa = {10, 20, 30, 40,40, 20, 50} #중복된 값이 저장되지 않음.
print(aaa)
