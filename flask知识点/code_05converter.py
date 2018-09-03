from flask import Flask
# BaseConverter  需要flask先高亮,才可以alt - enter
from werkzeug.routing import BaseConverter
# app = Flask(__name__, static_url_path="/sfsdsfd",static_folder="static")  # ValueError: urls must start with a leading slash /
app = Flask(__name__)  # ValueError: urls must start with a leading slash /


class ReConverter(BaseConverter):
    regex = "[0-9]{5}"    # regex变量名不可以变,基类的变量名

app.url_map.converters["xxx"] = ReConverter   # 创建一个类，定义方法（正则regex），then 关联对象 app.url_map.converters["xxx"] = className


@app.route("/ind/<xxx:u_id>")  # :两边不可以有空格
def index(u_id):   # 传参数
    print(app.url_map)
    return "返回的参数 = %s" % u_id

if __name__ == '__main__':
    app.run(debug=True)
