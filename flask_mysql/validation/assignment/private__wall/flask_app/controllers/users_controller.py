from flask import render_template, redirect, session, flash, request
from flask_app import bcrypt,app
from flask_app.models.user_model import User
from flask_app.models.message_model import Message



@app.route('/')
def index():
    if 'uuid' in session:
        return redirect('/dashboard')
    return render_template('index.html')


@app.route('/dashboard')
def dashboard():
    if 'uuid' not in session:
        return ('/')
    data = {
        'id':session['uuid']
    }
    users = User.show_all()
    messages = Message.my_message(data)
    user = User.show_one(data)
    return render_template('dashboard.html', users = users, messages=messages, user = user)

'''
********************************
ACTION ROUTES
********************************
'''

@app.route('/register', methods = ['POST'])
def register():
    if not User.validate_register(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        **request.form,
        'password':pw_hash
    }
    user = User.create(data)
    session['uuid'] = user
    return redirect('/dashboard')

@app.route('/login', methods = ['POST'])
def login():
    if not User.validate_login(request.form):
        return redirect('/')
    return redirect('/dashboard')

@app.route('/logout')
def logout():
    del session['uuid']
    return redirect('/')