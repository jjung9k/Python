# try:
#     number_a= int(input("정수 입력: "))
# except:
#     print("정수를 입력하지 않았습니다.")
# else: 
#     print("원의 반지름: ", number_a)
#     print("원의 둘레: ", 2*3.14*number_a)
#     print("원의 넓이: ", 3.14 * number_a * number_a)
# print()
# #----finally 구문
# try:
#     number_a= int(input("정수 입력: "))
 
#     print("원의 반지름: ", number_a)
#     print("원의 둘레: ", 2*3.14*number_a)
#     print("원의 넓이: ", int(3.14 * number_a * number_a))
# except:
#     print('정수를 입력하지 않았습니다.')
# else:
#     print('예외가 발생하지 않았습니다.')
# finally:
#     print("일단 프로그램이 어떻게든 끝났습니다.")
# print()
# # 반복문과 함께 사용하는 경우

# while True:
#     try:
#         print('try 구문이 실행되었습니다.')
#         break
#         print('try 구문의 break 키워드 뒤 입니다.')
#     except:
#         print('except 구문이 실행 되었습니다.')
#     finally:
#         print('finally 구문이 실행 되었습니다.')
#     print('while 반복문의 마지막 줄입니다.')
# print('프로그램이 종료 되었습니다.')
# print()

#확인문제 2
# n = [52, 273, 32, 103, 90, 10, 275]

# print("#(1) 요소 내부에 있는 값 찾기")
# print(">> {}는 {} 위치에 있습니다.".format(52, n.index(52)))
# print()

# print("#(2) 요소 내부에 없는 값 찾기")
# n1 = 500
# try:
#     print(">> {}는 {} 위치에 있습니다.".format(n1, n.index(n1)))
# except:
#     print('>> 리스트는 내부에 없는 값 입니다')
# print()

# print('--- 정상적으로 종료 되었습니다. ----')
# print()

#여러가지 예외가 발생할 수 있는 코드
# list_number = [52, 273, 32, 72, 100]

# try:
#     number_input = int(input("정수 입력: "))
#     print("{}번째 요소: {}".format(number_input, list_number[number_input])) # 리스트의 요소를 출력
# except Exception as exception:
#     print("type(exception):", type(exception))
#     print("exception:", exception)
# print()

#예외 구분하기
# list_number = [52, 273, 32, 72, 100]
# try:
#     number_input= int(input("정수 입력: "))
#     print("{}번째 요소: {}".format(number_input, list_number[number_input]))
# except ValueError:
#     print("정수를 입력해 주세요!")
# except IndexError:
#     print("리스트와 인덱스를 벗어났어요!")
# print()

#조건문의 기본 사용
number = input("정수 입력: ")
number = int(number)

if number > 0:
    print("양수입니다")
if number < 0:
    print("음수입니다")
if number == 0:
    print("0 입니다.")
print()
