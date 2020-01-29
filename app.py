from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session
from databases import *
 
app=Flask(__name__)
app.secret_key="MY_SUPER_SECRET_KEY"


@app.route('/', methods =["GET","POST"])
def signIN():
    if request.method == "GET":
       return render_template('signin.html')
    else:
        username = request.form["uname"]
        password = request.form["psw"]
        s=signin(username,password)
        if s:
            return render_template("index.html")
        else:
            print("try again")

            return render_template('signin.html')

@app.route('/signup',methods=["POST","GET"])
def signUp():
    if request.method == "GET":
        return render_template('signup.html')
    else:
        save(request.form['email'],request.form['psw'])
        return redirect(url_for('signIN'))

@app.route('/index')
def index():
    return  render_template('index.html')
 
@app.route('/about-us')
def hello():
    return render_template ('about-us.html')

@app.route('/contact', methods=["GET","POST"])
def contact():
	if request.method == "GET":
		return  render_template ('contact.html')
	else:
		username = request.form['uname']
		password = request.form["psw"]
		save(username,password)
		return render_template('index.html',
			u = username,
			p = password
			)

 
app.run(debug = True)