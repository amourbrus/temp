from flask import Flask,render_template
from flask_wtf import FlaskForm
from flask import request
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, EqualTo
app = Flask(__name__)

app.config["SECRET_KEY"]="HELOFFHShfh"


class RegisterF(FlaskForm):
    user_name = StringField(lable="用户名", validators=[DataRequired("must type into a user_name")])
    password = PasswordField(label="mima",validators=[DataRequired("must type into a password")])
    password2 = PasswordField(label="check",validators=[DataRequired("not same one ,wrong~")])
    sbt = SubmitField(label="submit to")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "get":
        data = RegisterF()
        return render_template("code_03wtf.html",  form=data)
    else:
        data = RegisterF()
        if data.validate_on_submit():
            return "success"
        else:

            return render_template("code_03wtf.html", form = data)

if __name__ == '__main__':
    app.run()

