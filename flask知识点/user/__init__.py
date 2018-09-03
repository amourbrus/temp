from flask import Blueprint


# user: 蓝图的名字, 注意斜杠 slash, 参数随便添加的玩
user_blue_obj = Blueprint("user", __name__, url_prefix="/itcast", )

# 这里只能在创建对象之后,在对象前则也会出现循环导入的问题
# from . import views
