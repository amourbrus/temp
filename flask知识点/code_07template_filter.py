from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index():
    data = {
        "name": "jack",
        "age": 19
    }
    return render_template("code_07.html", data = data)


# 自定义filter  ways 1 > @app.add_template_filter("li")
# @app.add_template_filter("li")   # 错误add
# @app.template_filter('li')
def do_step(xxx):
    return xxx[::2]
app.add_template_filter(do_step, "li")  # ways 2, 函数名，自定义过滤器的名字

if __name__ == '__main__':
    app.run(debug=True)

# 注意templates的“s”
# 没有提示,设置setting>language & framework > python template language
