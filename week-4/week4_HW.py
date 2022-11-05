from cgi import test
from cgitb import html
from distutils.log import error
from flask import Flask, request, render_template, session, url_for, redirect
app = Flask(__name__)

app.secret_key = 'wehelpassignmenttry1234'


@app.route('/')
def home():
    return "Hello,world!"


@app.route('/login')
def welcome():
    return render_template('login.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        if request.form['username'] == 'test' and request.form['password'] == 'test':
            session['id'] = username
            return redirect(url_for('member'))
        if request.form['username'] == "" or request.form['password'] == "":
            return redirect(url_for('error', message='請輸入帳號、密碼'))
        else:
            return redirect(url_for('error', message='帳號、或密碼輸入錯誤'))
    return render_template('login.html', error=error)


@app.route("/signin", methods=["GET", "POST"])
def signin():
    if "id" in session:
        return render_template("member.html", id=session["id"])
    return render_template("login.html")


@app.route('/error')
def error():
    msg=request.args.get("message","")
    return render_template("error.html", msg=msg)



@app.route("/signout", methods=["GET"])
def signout():
    session.pop('id', None)
    session.clear()
    return redirect("login")


@app.route('/member')
def member():
    if 'id' not in session:
        return redirect('login')
    return render_template('/member.html')


if __name__ == '__main__':
    app.run(port=3000)
