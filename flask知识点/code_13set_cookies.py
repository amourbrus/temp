from flask import Flask, make_response
from flask import request

app = Flask(__name__)


@app.route('/baidu')
def set_cookie():
    resp = make_response("一个参数， 响应体")
    # set_cookie 方法， 注意","
    resp.set_cookie("name", "itheima", max_age=3600)
    resp.set_cookie("city", "sz")
    return resp


@app.route('/get_cookie')
def get_cookie():
    name = request.cookies.get("name")
    return name

if __name__ == '__main__':
    app.run()
