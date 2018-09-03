from flask import Flask
from user.views import user_blue_obj  # 1,导入蓝图对象

app = Flask(__name__)

app.register_blueprint(user_blue_obj)  # 2,注册蓝图对象


@app.route('/news')
def news():
    return "news"


@app.route('/')
def index():
    return "index"

if __name__ == '__main__':
    print(app.url_map)
    app.run()


# init 初始化一个蓝图对象， 业务函数导入该对象代替app  flask对象
# 1,导入蓝图对象    2,注册蓝图对象
