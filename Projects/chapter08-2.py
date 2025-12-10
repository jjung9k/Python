class Parent:
    def __init__(self):
        self.value = "테스트"
        print("Parent 클래스의 __init()__ 메소드가 호출 되었다.")
    def test(self):
        print("parent 클래스의 test() 메소드입니다.")


class Child(Parent):
    def __init__(self):
        super().__init__()

# Toolkit  - Tkinter 티킨터 위젯 (표준 라이브러리, 쉬운 사용성, 높은 이식성)
# 텍스트나 이미지를 화면에 표시하는 위젯 입니다.
# 텍스트 레이블 생성
tk.Label(root, text="안녕하세요.")
Label.pack()
#클릭시 
# 엔트리 (Entry) 
btn = tk.Button(root, text='확인', command= run)
btn.pack()


