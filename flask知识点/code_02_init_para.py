from flask import Flask  # 导入flask程序开发包

app = Flask(__name__)  # 初始化flask对象， 第一个参数模块的名称
# static_path="dfafasfdadfasf",# 静态文件的路径
# static_url_path="",# 静态文件的路径 ,和static_path表示的就是一个意思
# static_folder="xxx",# 静态文件夹的名字
# template_folder="templates"# 模板文件夹的名字


@app.route('/')  # 定义理由和视图函数，路由地址随意取
def index_ha():
    return "hello world, what funny"

if __name__ == '__main__':  # 判断当前是否是入口
    # 打印当前所有的url地址
    # Map([ < Rule'/'(GET, HEAD, OPTIONS) -> index >,
    # < Rule'/static/<filename>'(GET, HEAD, OPTIONS) -> static >])
    print(app.url_map)
    app.run(host="192.168.88.131",port=8000)   # 启动flask程序  建议大家不要修改ip,port
