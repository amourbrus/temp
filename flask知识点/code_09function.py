# 控制代码块，control code block
from flask import flash

from flask import Flask, render_template
from flask import g

app = Flask(__name__)


# flash need SECRET_KEY, because it use session in flask
class Config(object):
    SECRET_KEY = "hfjajoi"

app.config.from_object(Config)


@app.route("/")
def index():
    g.name = "xxxitcsst"

    mylist = [
        {
            "id": 1,
            "value": "i love working"
        },
        {
            "id": 2,
            "value": "工作诗人"
        },
        {
            "id": 3,
            "value": "drowning in work"
        },
        {
            "id": 4,
            "value": "drowning in work"
        },
    ]
    # no need to do like mylist=mylist, use inner function get_flashed_messages()
    flash("please type into your userId")
    flash("please type into your userId")
    flash("please type into your userId")
    # 前端代码要注意格式  endif  endfor, use tab to solve this potential problem
    # for tab  --- if tab   that is it
    return render_template("code_04control.html", mylist=mylist)

if __name__ == '__main__':
    app.run(debug=True)

