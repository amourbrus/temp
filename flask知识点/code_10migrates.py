from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

# TODO 导入flask， 数据库falsk_sqlalchemy, 数据库迁移migraet, migratecommand, 脚本manager
# flask对象
app = Flask(__name__)


class Config(object):
    # TODO 1, 数据库连接，设置
    # coming from falsk_sqlalchemy  .py
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# 完成配置
app.config.from_object(Config)
# 数据库对象
db_obj = SQLAlchemy(app)
# 管理flask对象
manager = Manager(app)
# flask对象， 数据库对象交给Migrate,
Migrate(app, db_obj)
manager.add_command("db_alias", MigrateCommand)


# TODO 2. 建两张表
class User(db_obj.Model):
    __tablename__ = "users"
    id = db_obj.Column(db_obj.Integer, primary_key=True)
    name = db_obj.Column(db_obj.String(128))
    email = db_obj.Column(db_obj.String(128))
    password = db_obj.Column(db_obj.String(128))
    title = db_obj.Column(db_obj.String(128))
    # 多的一方设立外键， 参数为绑定的另一方 （表名.一个关联属性），一般是id
    role_id = db_obj.Column(db_obj.Integer, db_obj.ForeignKey("role.id"))

    # 供查询时友好提示
    def __repr__(self):
        return "User = %s, id = % s" % (self.name, self.id)


class Role(db_obj.Model):
    __tablename__ = "role"
    id = db_obj.Column(db_obj.Integer, primary_key=True)
    name = db_obj.Column(db_obj.String(128))
    # relationship 建立关系，和外键一起使用，供互查使用   第一个参数关联表对象（类名）， TODO 第二个参数给所关联的表使用,随便取，查询得到的值是__repr__返回值
    role_user = db_obj.relationship("User", backref="role")

    def __repr__(self):
        return "Role = %s, id = %s" % (self.name, self.id, )


@app.route('/')
def index():
    return "index page @@@@"

if __name__ == '__main__':
    db_obj.drop_all()
    # todo 迁移时，需要空的数据库！！
    # db_obj.create_all()
    #
    # ro1 = Role(name='admin')
    # db_obj.session.add(ro1)
    # db_obj.session.commit()
    # # 再次插入一条数据
    # ro2 = Role(name='user')
    # db_obj.session.add(ro2)
    # db_obj.session.commit()

    # us1 = User(name='wang', email='wang@163.com', password='123456', role_id=ro1.id)
    # us2 = User(name='zhang', email='zhang@189.com', password='201512', role_id=ro2.id)
    # us3 = User(name='chen', email='chen@126.com', password='987654', role_id=ro2.id)
    # us4 = User(name='zhou', email='zhou@163.com', password='456789', role_id=ro1.id)
    # us5 = User(name='tang', email='tang@itheima.com', password='158104', role_id=ro2.id)
    # us6 = User(name='wu', email='wu@gmail.com', password='5623514', role_id=ro2.id)
    # us7 = User(name='qian', email='qian@gmail.com', password='1543567', role_id=ro1.id)
    # us8 = User(name='liu', email='liu@itheima.com', password='867322', role_id=ro1.id)
    # us9 = User(name='li', email='li@163.com', password='4526342', role_id=ro2.id)
    # us10 = User(name='sun', email='sun@163.com', password='235523', role_id=ro2.id)
    # db_obj.session.add_all([us1, us2, us3, us4, us5, us6, us7, us8, us9, us10])
    # db_obj.session.commit()

    manager.run()


"""
数据库的操作：
# 查询所有all()，查询一个get(id)
In [18]: User.query.all()
Out[18]:
[User = wang, id = 1,
 User = zhang, id = 2,
 User = chen, id = 3,
 User = itcast, id = 5,
 User = wu, id = 6,
 User = qian, id = 7,
 User = liu, id = 8,
 User = li, id = 9,
 User = sun, id = 10]
# 互查 relationship
In [8]: Role.query.get(1)
Out[8]: Role = admin, id = 1

In [9]: Role.query.get(1).role_user
Out[9]:
[User = wang, id = 1,
 User = zhou, id = 4,
 User = qian, id = 7,
 User = liu, id = 8]

In [2]: User.query.get(4)
Out[2]: User = zhou, id = 4

In [3]: User.query.get(4).role
Out[3]: Role = admin, id = 1
# 删除数据， 先查询
In [13]: user = User.query.get(4)
In [14]: db_obj.session.delete(user)
In [15]: db.session.commit()
# 更新数据， 先查询
In [21]: User.query.get(5).name="lizude"
In [22]: db_obj.session.commit()

In [26]: User.query.count()
Out[26]: 9
# 增加数据，和py文件中写的一样
In [33]: ro3 = Role(name='user')
In [34]: db_obj.session.add(ro3)
In [35]: db_obj.session.commit()

# order_by  id
In [27]: User.query.order_by(User.id.desc()).all()

# filter  & filter_by
In [28]: User.query.filter(User.email.endswith('163.com')).all()
Out[28]: [User = wang, id = 1, User = li, id = 9, User = sun, id = 10]

In [32]: User.query.filter(User.name=='lizude').first()
Out[32]: User = lizude, id = 5

"""
