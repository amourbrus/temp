from flask import Flask, json, jsonify
from flask import redirect, url_for
# 导包和初始化对象
app = Flask(__name__)


class Config(object):  # debug
    DEBUG = True
# config ctrl 右键，find查看所有默认参数,还有converter 同样操作
app.config.from_object(Config)
# 等价于app.run(debug=True)


@app.route("/index/<num>", methods=['POST', 'GET'])
# 传参<>, 请求method,不写则default get
def index(num):
    data = {"name": "python",
            "age": 18
            }
    print(app.url_map, "\n", num)
    return jsonify(data), 344
    # 表示把字典转成json字符串
    # return jsonify(data), 344   # 只有这两个参数 第一个参数：表示响应体，就是展示到页面给用户看的内容
    # 第二个参数表示状态码, 自定义状态码，可以不写


@app.route("/360buy")
def demo2():
    # redirect
    return redirect(url_for("index"))


if __name__ == '__main__':
    # app.run(host="579375", port=888, debug=True)  # 指定地址，建议不要修改
    app.run()
