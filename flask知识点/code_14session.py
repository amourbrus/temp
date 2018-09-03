from flask import Flask, session
app = Flask(__name__)

# flask 中用到session就要有SECRET_KEY
app.config["SECRET_KEY"]="LAFG  HFAUH"
# attention -- set_session first then get_session, otherwise bug


@app.route('/set_session')
def set_session():
    session["name"] = "itcast haah"
    return " set successful"


@app.route('/get_session')
def get_session():
    name = session.get("name")
    return name

if __name__ == '__main__':
    app.run()