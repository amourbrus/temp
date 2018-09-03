from flask import Flask, abort
from flask import request
from flask_script import Manager


app = Flask(__name__)
# -- script, terminal to run
# manager = Manager(app)


@app.route('/', methods=['get', 'post'])
def index():

    # 0.post form postman
    user_name = request.form.get("user_name")
    age = request.form.get("age")
    # 1.get ways for args-->http://127.0.0.1:5000/?city=newYork
    city = request.args.get("city")
    # 2.upload --> get files from client(post),when there is files.get,it must be posted,else other post can't done
    # picture = request.files.get("pic")
    # picture.save("./2.png")
    print("buy xiaomi8")
    print("buy oneplus6")
    print("buy smartisan3")
    # abort(404)  # 配合@app.errorhandler(404)，后面的不会执行
    print("buy samsung galaxy note9")
    return "%s,,,%s,,,%s" % (user_name, age, city)


@app.errorhandler(404)
def error_hander(rer):
    return "can't find the page 0.0 @.@ "


if __name__ == '__main__':
    app.run(debug=True)
    # manager.run()
