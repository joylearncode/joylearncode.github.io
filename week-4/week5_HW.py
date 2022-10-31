from cgi import test
from distutils.log import error
from flask import Flask, request, render_template, session, url_for, redirect
app=Flask(__name__)

app.secret_key = 'wehelpassignmenttry1234'

@app.route('/')
def home():
    return "Hello,world!"

@app.route('/login')
def welcome():
    return render_template('login.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    # error=None
    if request.method=='POST':
        username = request.form['username']       
        if request.form['username']=='test' and request.form['password']=='test':
            session ['id']=username
            return redirect(url_for('member'))
        if request.form['username'] == "" or request.form['password'] == "" :
            return redirect(url_for('error2'))
        else:
            return redirect(url_for('error', message='error_account'))
    return render_template('login.html', error=error)

@app.route("/signin", methods=["GET","POST"])
def signin():
  if "id" in session: 
    return render_template("member.html", id=session["id"])
  return render_template("login.html") 
    

@app.route('/error')
def error():
    print(request.form.get('messasge'))
    return render_template('/error.html')

@app.route('/error2')
def error2():
    return render_template('/error2.html')

@app.route("/signout", methods=["GET"])
def signout():
  session.pop('id',None)
  session.clear()
  return redirect("login")

@app.route('/member')
def member():
    if 'id' not in session:
        return redirect('login')
    return render_template('/member.html')

if __name__=='__main__':
    app.run(port=3000)