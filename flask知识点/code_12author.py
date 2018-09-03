from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy

# summary ---1> 建数据库，config -2> create table--class Book ,class Author
# 3> 添加数据  4> index page  show 出数据 and 设置添加功能----书和作者和表单class AuthorBookForm ,
# 模板中读出表单-- ， 模板中读出数据 5. 分别删除书和作者 ， 通过模板中设置超链接地址，路由
# 注意 删除作者时，需要先删除书
# 低级错误 1. commit()拼错， 2. 模板中是 author.books author的属性books not book,会导致读不出book


# 表的注意事项： 1. db.Model 2. one -->relationship and plus --> db.Foreignkey
# 3. db.create_all()  really success
app = Flask(__name__)


# app.config["SECRET_KEY"]="SDFASH"
class Config(object):
    # 数据库
    SECRET_KEY = "DSFHADDFAS"
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/authorbook"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # app.config['SQLALCHEMY_ECHO'] = True

app.config.from_object(Config)
db = SQLAlchemy(app)


# 作者表
class Author(db.Model):
    __tablename__ = "authors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    books = db.relationship("Book", backref="author")


# 书表
class Book(db.Model):
    __tablename__ = "book"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    author_id = db.Column(db.Integer, db.ForeignKey("authors.id"))


class AuthorBookForm(FlaskForm):
    # 表单
    author_name = StringField(label="作者", validators=[DataRequired("请输入作者的名字")])
    book_name = StringField(label="书名", validators=[DataRequired("请输入作者的名字")])
    submit = SubmitField("添加")


# delete
@app.route('/delbook/<book_id>')
def delete_book(book_id):
    book = Book.query.get(book_id)
    db.session.delete(book)
    #  commit !!
    db.session.commit()
    return redirect(url_for("index"))


@app.route('/delauthor/<authorid>')
def delete_author(authorid):   # para,注意写上，and 不是author_id写成一样不要弄混
    author = Author.query.get(authorid)
    # book = Book.query.filter(Book.author_id == author.id).first()
    # db.session.delete(book)
    Book.query.filter(Book.author_id == author.id).delete()

    db.session.delete(author)
    db.session.commit()

    return redirect(url_for("index"))


@app.route('/', methods=['GET', 'POST'])
def index():
    # show 出数据----书和作者和表单
    form = AuthorBookForm()
    #  post submit content, add
    if form.validate_on_submit():
        author_name_data = form.author_name.data
        book_name_data = form.book_name.data

        author = Author()

        author.name = author_name_data
        db.session.add(author)
        db.session.commit()

        book = Book()
        book.name = book_name_data
        book.author_id = author.id
        db.session.add(book)
        db.session.commit()

    authors = Author.query.all()

    return render_template("code_12db.html", form=form, authors=authors)


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    # why add data fail?
    au1 = Author(name='老王')
    au2 = Author(name='老尹')
    au3 = Author(name='老刘')
    au4 = Author(name='miss')
    # 把数据提交给用户会话
    db.session.add_all([au1, au2, au3, au4])
    # 提交会话
    db.session.commit()
    bk1 = Book(name='老王回忆录', author_id=au1.id)
    bk2 = Book(name='我读书少，你别骗我', author_id=au1.id)
    bk3 = Book(name='如何才能让自己更骚', author_id=au2.id)
    bk4 = Book(name='怎样征服美丽少女', author_id=au3.id)
    bk5 = Book(name='如何征服英俊少男', author_id=au4.id)
    # 把数据提交给用户会话
    db.session.add_all([bk1, bk2, bk3, bk4, bk5])
    # 提交会话
    db.session.commit()
    app.run()






