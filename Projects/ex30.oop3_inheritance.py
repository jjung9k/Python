# 상속 inheritance -- 이미 설계된 다른 class를 상속받아 새로운 멤버만 추가하는 문법

# 문법학습전에 대략적인.. 상속의 필요성을 보여주는 예

# 게임개발.. 로봇 캐릭터 필요 (이동 기능, 공격기능)
class Robot:
    #이동 기능
    def move(self):
        print('걸어간다. 아장 아장...')
    #공격기능
    def attack(self):
        print('주먹 발사!!')
    
#Robot 객체 생성
r= Robot()
r.move()
r.attack()
print()

r2= Robot()
r2.move()
r2.attack()
print()

#캐릭터 종류를 추가.. [공중유닛].. 나는 로봇
#FlyRobot 설계 [ 이동, 공격, fly 플라이 기능] (Robot 기능 + 날수 있는 플라이기능)
# 원래 있던 Robot 클래스에 나는 기능을 추가하면.. 모든 로봇이 나는 기능이 생겨버림..그럼 안 됨.
# 그렇다는 것은 다른 종류의 제품이라는 것이니.. 별도의 설계도면이 필요함...

class FlyRobot:
    # 이동기능
    def move(self):
        print('걸어간다. 아장 아장...')
    # 공격기능
    def attack(self):
        print('주먹 발사!!')
    # 나는기능
    def fly(self):
        print("날아서 이동!~~")

fr= FlyRobot()
fr.move()
fr.attack()
fr.fly()
print()

# 또 새로운 캐릭터 추가..[해상유닛]  ---- 수영하는 로봇이 있었으면..[Robot기능 + 수영기능]
# 새로운 유닛이니.. 새로운 설계도(class)를 만들어야 함.
class SwimmingRobot(Robot):  # Robot 클래스의 기능들을 굳이 직접 다시 작성하지 않고 그대로 가져오기(상속 inheritance)
    #이미 [이동, 공격] 기능ㅇ르 보유한 상태임
    #새로운 기능만 추가하면 됨
    def swimming(self):
        print('음~파 음~파')

sr= SwimmingRobot()
sr.move() #만든 적이 없는 메소드.. Robot 클래스에 있던 메소드를 상속받아 내것인양 사용!!
sr.attack()  #상속받은 메소드
sr.swimming() #새로 추가한 메소드

# SwimmingRobot의 경우 Robot(기본기능)을 상속받았기에 기능 구현을 직접 안해도.. 편하게 물려받아 내것인양 사용가능!!!
print('-'*30)
print()

# 상속 문법 조금 더 알아보기
# First - Second

class First: 
    #생성자를 만들어서 멤버변수 a 만들기
    def __init__(self):
        self.a= 10
        print('First 객체가 생성 되었습니다.')

    #멤버변수를 출력 기능 메소드
    def show(self):
        print('a: ', self.a)

class Second(First): 
# 이미 First의 멤버들 [a, show()] 를 보유한 상태
    
# Second 클래스도 본인의 멤버변수를 만들기 위해 초기화 영역(생성자 함수) 추가하기
    def __init__(self):
        super().__init__() # 명시적으로 상속해 준 클래스의 생성자 함수를 호출해줘야만 함. 반드시 [super()이 상속해준 클래스 객체를 의미함]
        self.b= 20
        print('Second 객체를 생성했습니다.')

    #멤버값 출력기능 만들기... [기존에 있는 show() 기능이 맘에 들지 않아서.. 그래서 다시 만들기 override]
    def show(self):
        #상속해 준 멤버 a의 출력은 그 클래스의 가능으로 출력하는 것을 권장
        super().show() #First 의 show()가 발동
        print('b: ', self.b)


#Second 객체 생성
s= Second()  #상속해준 first 객체도 같이 생성 됨
# 상속해준 First 의 멤버를 사용
print(s.a)  #상속이라는 문법의 진정한 의미는 상속해 준 First 객체의 멤버를 마치 내것인양 사용할 수 있도록 해주는 문법 
print(s.b)  # Second에서 새로 만든 변수, b도 내 것인양 사용하는 변수
# 멤버값을 출력하는 기능을 사용해 보기
# s.show()  #상속받은 멤버출력 기능을 내것인양 호출해 보기..[ 새로 추가된 Second의 b 변수를 출력하지 않음.]
# show() 기능을 오버라이드(override) 하여... 개선 된 기능 사용
s.show()
print()

# 상속과 오버라이드 메소드 사용에 대한 마지막 연습 예제
# 예) 어떤 대학 웹사이트의 회원데이터 저장 [ 회원종류 여러개... ]

# 일반회원 : 이름, 나이
# 학   생 :  이름, 나이, 전공
# 교   수 :  이름, 나이, 연구과제
# 근로학생 : 이름, 나이, 전공, 업무

# 일반회원 데이터를 저장하기 위한 클래스 설계
class Person:
    def __init__(self, name, age):
        self.name= name
        self.age= age
        print('Person 객체 생성')

    def show(self):
        print('이름: ', self.name)
        print('나이: ', self.age)
p= Person('sam', 20)
p.show()
print()

#학생 회원 정보 저장을 위한 Student클래스를 설계 및 생성 [ Person 클래스를 상속해서 ]
class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major= major
        print('Student 객체 생성')

    #전공 정보도 출력하는 기능으로 show()를 개선
    def show(self):
        super().show() # 이름, 나이 출력
        print('전공: ', self.major)

s= Student('robin', 23, 'ai web')
s.show()
print()

#교수 회원 [ 일반 회원 + 연구 과제 ] 
class Professor(Person): 
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject= subject
        print('Professor 객체 생성')
        print()

# 연구과제가지 함께 출력하는 기능으로 show() 개선
    def show(self):
        super().show()
        print('연구과제: ', self.subject)

pro= Professor('park', 45, 'ai data analysis')
pro.show()
print()

#근로학생 클래스 설계 및 생성  [ 학생회원 + 업무 ]
class ScholarshipStudent(Student):
    def __init__(self, name, age, major, task):
        super().__init__(name, age, major)
        self.task= task
        print('Scholargship 객체 생성')
        print()

    #업무까지 출력해 주는 기능으로 개선
    def show(self):
        super().show()
        print('업무: ', self.task)

scholar= ScholarshipStudent('hong', 25, 'data analysis', 'pc management')
scholar.show()
    