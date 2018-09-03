from flask import Flask

app = Flask(__name__)


@app.route('/index')
def index():
    return "index page"


# hook  请求钩子，用于在index 函数执行完成或前完成，掌握执行的顺序
# 第一次请求之前执行（只执行一次）
@app.before_first_request
def handler_be_first_re():
    print("handler_before_first_request")


# 在请求index函数之前执行（每次都会执行）
@app.before_request
def handler_before_request():
    print("handler_before_request")


# 在index函数执行完成之后执行 -- 如果当前程序报错就不会执行
# 注意response
@app.after_request
def handler_after_req(response):
    print("handler_after_request")
    return response


# 在index函数执行完成之后执行  -- after_request执行完成之后再执行
# 注意参数 error ---TypeError: handler_teardown_request() takes 0 positional arguments but 1 was given
@app.teardown_request
def handler_teardown_request(e):
    print("handler_teardown_request")

if __name__ == '__main__':
    app.run()