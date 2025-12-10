#객체를 만드는 함수(1)
def create_stu(name, kor, math, eng, sci):    # #딕셔너리를 리턴하는 함수를 선언합니다.
    return {
        "name": name, 
        "kor": kor,
        "math": math,
        "eng": eng,
        "sci": sci
        }
 # 학생 리스트를 선언 합니다.
students = [           
    create_stu("윤인성", 87, 98, 88, 95),
    create_stu("연하진", 92, 98, 96, 98),
    create_stu("구지연", 76, 96, 94, 90),
    create_stu("나선주", 98, 92, 96, 92),
    create_stu("윤아린", 95, 98, 98, 98),
    create_stu("윤명월", 64, 88, 92, 92)
]
# 학생을 한명씩 반복 합니다.
print("이름", "총점", "평균", sep="\t")  
for student in students:
    score_sum= student['kor'] + student['math'] + student['eng']+\
        student['sci']
    score_average= score_sum/4
    print(student['name'], score_sum, score_average, sep='\t')
print()

#객체를 만드는 함수(2)
    
def create_stu(name, kor, math, eng, sci):    # #딕셔너리를 리턴하는 함수를 선언합니다.
    return {
        "name": name, 
        "kor": kor,
        "math": math,
        "eng": eng,
        "sci": sci
        }
# 학생을 처리하는 함수를 선언한다.
def student_get_sum(student):
    return student['kor'] + student['math'] + \
        student['eng'] + student['sci']

def student_get_average(student):
    return student_get_sum(student) / 4

def student_to_string(student):
    return "{}\t{}\t{}".format(student['name'],
    student_get_sum(student),
    student_get_average(student))             

students = [ 
    create_stu("윤인성", 87, 98, 88, 95),
    create_stu("연하진", 92, 98, 96, 98),
    create_stu("구지연", 76, 96, 94, 90),
    create_stu("나선주", 98, 92, 96, 92),
    create_stu("윤아린", 95, 98, 98, 98),
    create_stu("윤명월", 64, 88, 92, 92)
]

print('이름', '총점', '평균', sep='\t')  # sep는 "separator"의 약자, 매개변수이다.
for student in students:
    print(student_to_string(student))
print()


#클래스 내부에 함수(메소드) 선언하기
class Student:
    def __init__ (self, name, kor, math, eng, sci):
        self.name= name
        self.kor= kor
        self.math= math
        self.eng= eng
        self.sci= sci
    def get_sum(self):
        return self.kor + self.math + self.eng + self.sci
    
    def get_average(self):
        return self.get_sum() / 4
    
    def to_string(self):
        return "{}\t{}\t{}".format(
           self.name,
           self.get_sum(),
           self.get_average())
    
    #학생 리스트를 선언 합니다. (☆들여쓰기 없음☆)
students = [ 
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92)
       ]

#학생을 1명씩 반복 한다.
print("이름", "총점", "평균", sep='\t')
for student in students:
    print(student.to_string())
print()