# 파이썬에서 대량의 데이터를 다루는 문법 [ List, Tuple, Dictionary, {set}]

# 대량의 데이터를 다루는 문법이 별도로 등장한 이유.. 알아보기...

# 학생 3명의 성적데이터를 저장.. 
# a= 70
# b= 80
# c= 90

# # 데이터를 출력하려면...
# print(a, b, c)

# #반복문으로 해결 안됨... 왜? 변수이름이 서로 달라서..

# # 이런 학생의 수가.. 15명이면... ?? 만약 150명이면..

# # 이때 리스트 같은 대량의 데이터를 다루는 문법이 있다면...

# aaa= [70, 80, 50, 60, 70, 80, 90, 100]
# print(aaa)
# print(aaa[0])
# total= 0 
# for e in aaa:
#     print(e)
#     total = total+e
# print()
# print('-'*30)


# 1. List [] - 요소의 값 변경 및 추가/삭제 가능
aaa= [10, 20, 30, 40] # 용어: 인덱스, 요소
# 리스트를 저정한 변수를 출력하면 그 안에 있는 값들을 모두 보여줌.
print( aaa )
# 자료형을 확인해 보기
print( type(aaa))
print()
# 요소값 개별사용 - 인덱스 번호
print( aaa[0] ) # 변수 이름을 쓰고 대괄호 만들고, 인덱스는 하나만 써야 한다.
print( aaa[1] )
print( aaa[2] )
print( aaa[3] )
#print( aaa[4] ) # 범위에 벗어나 숫자는 error 가 난다.
print()

# 요소의 개수가 많으면.. 인덱스번호를 직접 쓰기 복잡하다. 반복문으로 해결
for n in range(4): # [0, 1, 2, 3]
    print(aaa[0])
print()

#for 문법의 대량의 데이터에서 요소를 반복적으로 뽑아오는 것임. 인덱스번호를 뽑지 말고, 그냥 바로 aaa 리스트의 요소를 뽑으면
for e in aaa:
    print(e)
print()

# 역순으로 출력하고 싶다면... 특정 범위만 출력하려면..
for n in range(3,-1, -1):
    print(aaa[n])
print()

# 역순2번째 방법
for n in range(4):  #0,1,2,3
    print(aaa[3-n]) #3,2,1,0
print()

#1~3번 방의 요소만 출력. [범위 출력]
for n in range(1,4):  #1,2,3
    print(aaa[n])
print()

# 모든 요소값들에 1을 더한 값을 출력하세요.. 요청
for e in aaa:
    print(e+1)
print()

# 모든 요소값을 더한 총합계산도 가능.
total= 0
for e in aaa:
    total = total + e
print('총합: ', total)
print()

#리스트의 요소들 중에서 가장 큰 최대값...
# if aaa[0]>aaa[1]


print()

m = aaa[0]
if m<aaa[1]: m= aaa[1]

if m<aaa[2]: m= aaa[2]

if m<aaa[3]: m= aaa[3]
print(m)

m= aaa[0]
for n in range(1, 4):
    if m<aaa[n]: m= aaa[n]
print(m)

max(aaa)
print()
print('-'*30)
print()

#요소값 변경 - 인덱스 번호 사용
aaa[0] = 100  
print( aaa )

# 요소 추가 - append(), insert()
# aaa[4]= 50

aaa.append(70) # 70이라는 값을 리스트의 마지막에 추가
print( aaa ) 

print(aaa[2])
aaa.insert(1, 600) # 1번 인덱스 위치에 600이라는 값을 삽입
print( aaa )
print(aaa[2])
print()

# 요소 삭제 - remove(), de1 연산자, clear()
aaa.remove(100) #100이라는 값을 가진 요소를 제거
print()

del aaa[2] # aaa[2] 요소를 제거
print(aaa)

# aaa.clear() # 전체를 삭제할 때
# print(aaa)

# 요소의 개수를 알려주는 파이썬의 내장 기능 함수 len()
print('요소 개수 : ',len(aaa))

# 요소들의 자료형이 달라도 상관없음.
aaa = [10, 3.14, False, 'sam']
print(aaa)

# 반복문으로 접근 가능
for e in aaa:
    print(e)
print()

# 리스트가 가진 유용한 여러 기능함수들 소개..
#1) 요소의 순서를 뒤집기
aaa.reverse() #원본 리스트가 변경 됨(매우 중요함)
print(aaa)

#2) 요소 정렬
aaa = [4,15,7,2,16,4,10,4]
aaa.sort()
print(aaa)
#3) 요소 중 특정 값의 인덱스 번호(위치) 얻어오기
idx= aaa.index(16) #16이라는 숫자가 있는 위치번호(인덱스 번호)
print(idx)

#4) 특정값이 리스트안에 있는지 여부.. in 연산자
print( 7 in aaa )
print( 70 in aaa )
print( 5 not in aaa) #있지 않니..

#5) 특정값이 리스트안에 몇개 인지...
print( aaa.count(4), "개")

#6) 특정값이 꺼내오기... 원본에서 없어지는 것임
n = aaa[2] #이건 사용하는 것.
print(n)
print(aaa)

n= aaa.pop(2) #이게 꺼내오는 것임
print(n)
print(aaa)

#7) 다른 리스트를 한방에추가하기... [리스트의 확장]
aaa= [10, 20, 30]
bbb= [4,5,6]

aaa.extend(bbb)
print(aaa)

# .extend() 기능 잘사용안 함. 왜? + 연산을 하면 리스트 확장기능이 발동함
ccc=[700,800,900]
print(aaa+ccc)

#--------------------------------------#qks

# 2차원 리스트 --- 리스트의 요소가 또 다른 리스트인 것..
aaa = [
     [10,20,30],
     ['aa', 'bb'],
     [3.14, 12.2, 300, 500]
]
print(aaa)
print(aaa[0])
print(aaa[0][0])
print(aaa[1][0])

# len() 기능은.. 리스트의 요소개수를 알려 줌.
print(len(aaa))
print(len(aaa[0]))
print(len(aaa[1]))
print(len(aaa[2]))
print()

# 각 요소값들 접근,, 하여 사용
print(aaa[0][0], end='\t')
print(aaa[0][1], end='\t')
print(aaa[0][2], end='\t')
print()

print(aaa[1][0], end='\t')
print(aaa[1][1], end='\t')
print()

#반복문으로 위 작업 처리
a = len(aaa[0])
for n in range(a): #0,1,2
    print(aaa[0][n], end='\t')
print()

a = len(aaa[1])
for n in range(a): #0,1
    print(aaa[1][n], end='\t')
print()

a = len(aaa[2])
for n in range(a): #0,1,2,3
    print(aaa[2][n], end='\t')
print()

# 각 줄을 출력하는 3개의 덩어리를 반복문으로 줄이기...
for k in range(3):
    a = len(aaa[k])
    for n in range(a): #0,1,2,3
        print(aaa[k][n], end='\t')
    print()
print()

#[row : 행(줄), column:열(칸)]
for row in aaa:
    for column in row:
        print(column, end='/t')
    print()
print()

# 리스트를 사용하여 여러데이터를 다루는 예제 해 보기
# 예제1) 학생의 성적들의 총합과 평균 구하기
score_list= [80,75,64,90,50]
total = 0
for score in score_list:
    total= total + score

print('총점: ', total)
print('평균: ', total/len(score_list))
print()

#예2) 일주일의 온도 중에서 가장 더운 날의 온도와 요일은? (데이터의 순서: [월,화,수,목,금,토,일])
week_temparature= [15, 8, 16, 9, 7, 6, 10]
highest= week_temparature[0]
for temp in week_temparature:
    if highest<temp: highest= temp

print('최고온도: ', highest)

idx= week_temparature.index(highest)
print(idx)

if idx==0:
    print('월요일')
elif idx==1:
    print('화요일')
elif idx==2:
    print('수요일')   
elif idx==3:
    print('목요일')
elif idx==4:
    print('금요일')
elif idx==5:
    print('토요일')
elif idx==6:
    print('일요일')
#----------------------------------
week= ['월요일','화요일','수요일','목요일', '금요일', '토요일']
       
       
