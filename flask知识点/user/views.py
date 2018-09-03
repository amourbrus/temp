# from . import user_blue_obj
from user import user_blue_obj
# 两个等价

# 这里写views的业务，user_blue_obj代替app
@user_blue_obj.route("/user")
def user():
    return "user page"
