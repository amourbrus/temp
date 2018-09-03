from flask import Flask, current_app

app = Flask(__name__)

class Config(object):
    DEBUG = True   # 开启调试模式

    ITCAST = "python"   # 如果放到config文件里面的代码需要大写
    
app.config.from_object(Config)    # 从对象加载(重点), 通过app对象关联当前的config这个类

# 从文件加载(了解), 加引号-----app.config.from_pyfile("config.cfg")

@app.route('/')
def index():
    print(current_app.config.get("ITCAST"))  # current_app是app的一个代理对象
    return "index page"

if __name__ == '__main__':
    app.run()