# 플라스크 import 
from flask import Flask

# 플라스크 객체 생성
app = Flask(__name__)           # __name__ 은 여기 파일 hello를 받아준다.

# 서버 구동시, 개발 정의 URL값과 플라스크에서 정의된 함수를 연결
# get + post 함수
@app.route("/hello2", methods = ['GET'])
def hello_flask_get():
    return "Get Method"

@app.route("/hello2", methods = ['POST'])
def hello_flask_post():
    return "Post Method"

@app.route("/hello/yg")
def hello_name():
    return "yg"

@app.route("/hello/jw")
def hello_name2():
    return "jw"

@app.route("/hello3/<name>")
def hello_name3(name):
    print(name)
    return name


    

# 해당 파일 실행시 플라스크 서버 실행           실행하면 __name__이 __main__으로 바뀌게 된다.
if __name__ == "__main__":
		app.run(host = "127.0.0.1", port = 5000, debug = True)

