from tkinter import *

# 이미지를 보여주는 위젯은 없음. 대신. Label 위젯에 text='' image=''로 보여줌

window= Tk()

# 이미지 파일의 경로를 써야 해서.. 
# 이미지 파일을 읽어서 파이썬에서 사용할 수 있는 객체로 만들어주는 클래스를 이용
img= PhotoImage(file='image/ms18.png').subsample(2)   #해상도를 줄여야 사이즈도 줄어듦. 2배 줄이기
# img= PhotoImage(file= 'image/paris.jpg')  #tkinter 의 PhotoImage()는 png, gif 파일만 가능하고 jpg는 사용불가!!
label= Label(window, Image=img)
label.pack()

# jpg 이미지를 보여 주고 싶다면,, 외부 라이브러리 추가( pillow [PIL 파이썬 이미지 라이브러리의 후속판])
# 설치 pip install pillow
# pillow library 사용

from PIL import Image, ImageTk  #Image: 이미지객체, Image TK; Tkinter에서 PIL Image를 사용할 수 있도록 해 줌
#PIL를 이용하여 이미지파일을 불러 오기
pil_image= Image.open('image/paris.jpg')
# 이미지 사이즈 변경 가능
pil_image= pil_image.resize((300,200), Image.LANCZOS)  #튜플타임으로 너비, 높이, 사이즈 조절할대 이미지품질 설정값
# pill_image를 Label 위젯에서 인식하지 못함. 그래서 변환
img2= ImageTk.PhotoImage(image=pil_image)

label2= Label(window, image=img2)
label2.pack()

# 버튼 클릭시에 이미지를 변경해 보기
# 버튼 클릭할때 변경할 이미지도 미리 준비
pil_image= Image.open('image/newyork.jpg')
pil_image= pil_image.resize((300, 200), Image.LANCZOC)
img3= imageTk.PhotoImage(image=pil_image)

def aaa():
    img= label2.cget('image')
    if img==str(img2):
        label2.configure(image=img3)
    else:
        label2.configure(image=img2)

btn= Button(window, text='change image', command=aaa)
btn.pack()






window.mainloop()

