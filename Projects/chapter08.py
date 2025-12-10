class Student:
    def study(self):
        print('공부를 한다.')
class Teacher:
    def teach(self):
        print('학생을 가르친다')
# 교실 내부의 객체 리스트를 생성합니다.
classroom = [Student(), Student(), Teacher(), Student(), Student()]

#반복을 적용해서 적절한 함수를 호출하게 합니다.
for person in classroom:
    if isinstance(person, Student):
        person.study()
    elif isinstance(person, Teacher):
        person.teach()
print()
#__srt__() 함수 손코딩 해 보기
class Student:
    def __init__(self, name, kor, math, eng, sci):
        self.name= name
        self.kor= kor
        self.math=math
        self.eng=eng
        self.sci=sci

    def get_sum(self):
        return self.kor + self.math +\
        self.eng + self.sci
    def get_average(self):
        return self.get_sum() / 4
    #__st__ () 라는 이름으로 함수를 선언 했음
    def __str__(self):
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(),
            self.get_average())
students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92)
]
print("이름", "총점", "평균", sep="\t")
for student in students:
    print(str(student))  # srt() 함수의 매개변수로 넣으면 student의 __str__()함수가 호출 된다.
print()

# 크기 비교 함수
class Student:   #클래스를 선언 합니다.
    def __init__(self, name, kor, math, eng, sci):
        self.name= name
        self.kor= kor
        self.math= math
        self.eng= eng
        self.sci= sci
    def get_sum(self):
        return self.kor + self.math +\
            self.eng + self.sci
    def get_average(self):
        return self.get_sum() / 4
    def __str__(self):
        return "{}{}{}".format(
            self.name,
            self.get_sum(),
            self.get_average()
        )
    def __eq__(self, value):
        return self.get_sum() == value.get_sum()
    def __ne__(self, value):
        return self.get_sum() != value.get_sum()
    def __gt__(self, value):
        return self.get_sum() > value.get_sum()
    def __ge__(self, value):
        return self.get_sum() >= value.get_sum()
    def __lt__(self, value):
        return self.get_sum() < value.get_sum()
    def __le__(self, value):
        return self.get_sum() <= value.get_sum()
    
students =[ 
        Student("윤인성", 87, 98, 88, 95),
        Student("연하진", 92, 98, 96, 98),
        Student("구지연", 76, 96, 94, 90),
        Student("나선주", 98, 92, 96, 92),
        Student("윤아린", 95, 98, 98, 98),
        Student("윤명월", 64, 88, 92, 92)
]

student_a= Student( "윤인성", 87, 98, 88, 95 )
student_b= Student( "연하진", 92, 98, 96, 98 )

print("student_a == student_b = ", student_a == student_b)
print("student_a != student_b = ", student_a != student_b)
print("student_a > student_b = ", student_a > student_b)
print("student_a >= student_b = ", student_a >= student_b)
print("student_a < student_b = ", student_a < student_b)
print("student_a <= student_b = ", student_a <= student_b)
print()

class Student:
    count = 0   # 클래스 변수 만들기

    def __init__(self, name, kor, math, eng, sci):
        #인스턴스 초기 변수화
        self.name= name
        self.kor= kor
        self.math= math
        self.eng= eng
        self.sci= sci

        #클래스 변수 설정
        Student.count += 1   # 클래스 변수에 접근하기 >> 클래스 이름.변수이름
        print("{}번째 학생이 생성되었습니다.".format(Student.count))

students = [ 
        Student("윤인성", 87, 98, 88, 95),
        Student("연하진", 92, 98, 96, 98),
        Student("구지연", 76, 96, 94, 90),
        Student("나선주", 98, 92, 96, 92),
        Student("윤아린", 95, 98, 98, 98),
        Student("윤명월", 64, 88, 92, 92)
]
print()
print("현재 생성된 총 학생 수는 {}명 입니다".format(Student.count))
print()
#클래스 함수

class Student:
    #클래스 함수
    count = 0
    students = []

    #클래스 함수
    @classmethod
    def print(cls):
        print("=========== 학생 리스트 =============")
        print("이름\t\t총점\t\t평균")
        for student in cls.students:
            print(str(student))
        print("====================================")

    def __init__(self, name, kor, math, eng, sci):
        self.name = name
        self.kor = kor
        self.math = math
        self.eng = eng
        self.sci = sci
        Student.count += 1
        Student.students.append(self)

    def get_sum(self):
        return self.kor + self.math + \
                self.eng + self.sci
    def get_average(self):
        return self.get_sum() / 4
    def __str__(self):
        return "{}\t\t{}\t\t{}".format(\
                self.name, \
                self.get_sum(), \
                self.get_average())
        
Student("윤인성", 87, 98, 88, 95)
Student("연하진", 92, 98, 96, 98)
Student("구지연", 76, 96, 94, 90)
Student("나선주", 98, 92, 96, 92)
Student("윤아린", 95, 98, 98, 98)
Student("윤명월", 64, 88, 92, 92)
Student("김미화", 82, 86, 98, 88)
Student("김연화", 88, 74, 78, 92)
Student("박아현", 97, 92, 88, 95)
Student("서준서", 45, 52, 72, 78)

Student.print()