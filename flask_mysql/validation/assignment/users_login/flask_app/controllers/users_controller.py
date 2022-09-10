from flask_app import app, bcrypt
from flask import render_template, redirect, request, flash, session

from flask_app.models.user_model import User

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods = ['POST'])
def register():
    if not User.validate(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "fname":request.form['fname'],
        "lname":request.form['lname'], 
        "password":pw_hash,
        "email":request.form['email'] 
    }
    user_id = User.add(data)
    session['uuid'] = user_id
    return redirect('/')

@app.route('/login', methods = ['POST'])
def login():
    if not User.validate_login(request.form):
        return redirect('/')
    return redirect('/success')

@app.route('/success')
def success():
    data = { 'email':session['user_email'] }
    user = User.find_user_by_email(data)

    return render_template('success.html', user = user)