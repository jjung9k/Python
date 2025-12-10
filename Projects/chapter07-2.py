#함수 데코레이터의 기본
def test(function):
    def wrapper():  
        print('인사가 시작되었습니다.')
        function()
        print('인사가 종료되었습니다.')
    return wrapper

@test          # @test는 hello() 함수에 포장(wrapper)을 씌우는 역할
def hello():    
    print("hello")

hello()
print()

# Beautiful Soup 스크레핑 실행해 보기
from flask import Flask
from urllib import request
from bs4 import BeautifulSoup

app = Flask(__name__)
@app.route("/")

def hello():
    target = request.urlopen('http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnID=108')

    soup = BeautifulSoup(target, "html.parser")

    output = ""
    for location in soup.select("location"):
        output += "<h3>{}<h3>".format(location.select_one("city").string)
        output += "날씨 : {}<br/>".format(location.select_one("wf").string)
        output += "최저/최고 기온: {}/{}"\
            .format(\
                location.select_one("tmn").string,\
                location.select_one("tmx").string\
                )
        output += "<hr/>"
    return output
print()
