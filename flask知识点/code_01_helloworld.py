from flask import Flask  # 导入flask程序开发包

app = Flask(__name__)  # 初始化flask对象， 第一个参数模块的名称


@app.route('/')  # 定义路由和视图函数，路由地址随意取
def index_ha():
    return "hello world, what funny"   # 返回给浏览器的客户端，给用户看

if __name__ == '__main__':  # 判断当前是否是入口
    app.run()   # 启动flask程序
