from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)

app.secret_key = 'wehelp12345'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'liang1009'
app.config['MYSQL_DB'] = 'database_6'

# Intialize MySQL
mysql = MySQL(app)

# 登入
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))
        account = cursor.fetchone()

        if account:
            session['loggedin'] = True
            session['name']=account['name']
            session['id'] = account['id']
            session['username'] = account['username']
            return redirect(url_for('member'))
        else:
            # Account doesnt exist or username/password incorrect
            return redirect(url_for('error',message='帳號或密碼輸入錯誤'))
    return render_template('index.html', msg=msg)

# 登出
@app.route('/signout')
def signout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    session.clear()
    return redirect(url_for('signin'))

# 註冊
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    msg = ''
    # Check if "username", "password" and "name" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'name' in request.form:
        # Create variables for easy access
        name = request.form['name']
        username = request.form['username']
        password = request.form['password']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'SELECT * FROM accounts WHERE username = %s', (username,))
        account = cursor.fetchone()
        if account:
            return redirect(url_for('error',message='帳號已被註冊'))
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = '帳號須包含英文字及數字!'
        elif not username or not password or not name:
            msg = '請填寫帳號及密碼!'
        else:
            cursor.execute(
                'INSERT INTO accounts VALUES (NULL, %s, %s, %s)', (name, username, password))
            mysql.connection.commit()
            msg = '註冊成功!'
    elif request.method == 'POST':
        msg = '請填寫表格!'
    return render_template('register.html', msg=msg)

# 登入成功
@app.route('/member')
def member():
    if 'loggedin' in session:
        return render_template('member.html', name=session['name'])
    return redirect(url_for('signin'))

# 錯誤頁面
@app.route('/error')
def error():
    msg=request.args.get("message","")
    return render_template("error.html", msg=msg)

if __name__ == '__main__':
    app.run(port=3000)
