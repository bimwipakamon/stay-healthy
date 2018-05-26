# views.py

from flask import render_template, flash, redirect, session, request, url_for
from stay_healthy.models import User, db, Contact
from stay_healthy import app
from functools import wraps
import os

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first")
            return redirect(url_for('login'))

    return wrap

# @app.route("/profile", methods=["GET", "POST"])
# @login_required

@app.route('/')
def index():
    username = session.get('username', '')
    return render_template("index.html",username=username)


@app.route('/standard-diet')
def standard():
    username = session.get('username', '')
    return render_template("standard.html",username=username)


@app.route('/vegetarian-diet')
def vegetarian():
    username = session.get('username', '')
    return render_template("vegetarian.html",username=username)


@app.route('/full-body-workout')
def fullBody():
    username = session.get('username', '')
    return render_template("fullBody.html",username=username)


@app.route('/abs-workout')
def abs():
    username = session.get('username', '')
    return render_template("abs.html",username=username)


@app.route('/butt-workout')
def butt():
    username = session.get('username', '')
    return render_template("butt.html",username=username)


@app.route('/arm-workout')
def arm():
    username = session.get('username', '')
    return render_template("arm.html",username=username)


@app.route('/leg-workout')
def workout_leg():
    username = session.get('username', '')
    return render_template("workout_leg.html",username=username)


@app.route('/bmi')
def bmi():
    username = session.get('username', '')
    return render_template("bmi.html",username=username)


@app.route('/bmr')
def bmr():
    username = session.get('username', '')
    return render_template("bmr.html",username=username)


@app.route('/body-fat')
def body():
    username = session.get('username', '')
    return render_template("body-fat.html",username=username)


@app.route('/ideal-weight')
def ideal():
    username = session.get('username', '')
    return render_template("ideal_weight.html",username=username)


@app.route('/daily-calorie')
def daily():
    username = session.get('username', '')
    return render_template("daily_calorie.html",username=username)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    error = None
    success = None
    username = session.get('username', '')
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        if name == "" or email == "" or message == "":
            error = "Please fill empty field."
        else:
            try:
                contact = Contact(name=name, email=email, message=message)
                db.session.add(contact)
                db.session.commit()
                success = "Your message was sent."
                flash("We got your message!!.", "success")

            except:
                db.session.rollback()
                error = "Something Wrong!"
                flash('Something Wrong!', 'error')

    return render_template("contact.html", username=username, error=error, success=success)

@app.route('/apple')
def apple():
    username = session.get('username', '')
    return render_template("apple.html",username=username)

@app.route('/avocado')
def avocado():
    username = session.get('username', '')
    return render_template("avocado.html",username=username)

@app.route('/banana')
def banana():
    username = session.get('username', '')
    return render_template("banana.html",username=username)

@app.route('/mangoes')
def mangoes():
    username = session.get('username', '')
    return render_template("mangoes.html",username=username)

@app.route('/mangosteen')
def mangosteen():
    username = session.get('username', '')
    return render_template("mangosteen.html",username=username)

@app.route('/orange')
def orange():
    username = session.get('username', '')
    return render_template("orange.html",username=username)

@app.route('/watermelon')
def watermelon():
    username = session.get('username', '')
    return render_template("watermelon.html",username=username)

@app.route('/register', methods=["GET", "POST"])
def register():
    session['username'] = ''
    error = None
    success=None
    if request.method == 'POST':
        username = request.form['txtUsername']
        password = request.form['txtPassword']
        name = request.form['txtName']
        if username == '' or password == '' or name == '':
            error = 'Please enter your username or password'
        else:
            if error == None:
                try:
                    new_user = User(username=username,
                                    password=password, name=name)
                    db.session.add(new_user)
                    db.session.commit()
                    session['username'] = username
                    session['password'] = password
                    session['name'] = name
                    success = "Register successfully."
                    flash('Register successfully.', 'success')
                    return redirect(url_for('.index'))
                except:
                    db.session.rollback()
                    error = "Username or Password already exists."
                    flash('Something Wrong!', 'error')
    return render_template("register.html", error=error, success=success,username=username)


app.secret_key = os.urandom(12)
@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    username = session.get('username', '')
    password = session.get('password', '')
    if request.method == 'POST':
        if request.form['txtUsername'] == '' and request.form['txtPassword'] == '':
            error = 'Please enter your username and password.'
        elif request.form['txtUsername'] == '':
            error = 'Please enter your username'
        elif request.form['txtPassword'] == '':
            error = 'Please enter your password'
        else:
            users = User.query.all()
            for user in users:
                if request.form['txtPassword'] == user.password and request.form['txtUsername'] == user.username:
                    flash('Login successfully.', 'success')
                    if username:
                        session['username'] = username
                    else:
                        session['username'] = request.form['txtUsername']
                    return redirect(url_for('.index'))
                else:
                    error = 'Invalid username or password. Please try again.'
    return render_template('login.html', error=error, username=username, password=password)


@app.route('/logout')
def logout():
    session['username'] = ''
    flash('You were logged out')
    return redirect(url_for('.index'))


