from flask_app import app, bcrypt
from flask import render_template, redirect, request, flash, session

from flask_app.models.users_model import User
from flask_app.models.party_model import Party


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/dashboard')
def dashboard():
    if 'uuid' not in session:
        return redirect('/')
    all_parties = Party.get_all()
    user_data = {
        'id':session['uuid']
    }
    logged_user = User.get_by_id(user_data)
    return render_template('dashboard.html', all_parties = all_parties, logged_user = logged_user)



'''
*******************ACTION ROUTE*********************
'''


@app.route('/users/register', methods=['POST'])
def register():
    if not User.validate(request.form):
        return redirect('/')
    hash_pass = bcrypt.generate_password_hash(request.form['password'])
    data = {
        **request.form,
        'password':hash_pass
    }
    id = User.create(data)
    session['uuid'] = id
    return redirect('/dashboard')

@app.route('/users/login', methods = ['POST'])
def login():
    data = {'email':request.form['email']}
    user_in_db = User.get_by_email(data)
    # print("*****************")
    if not user_in_db:
        print("*****************")
        flash('Invalid login info', 'log')
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['pw']):
        print("*****************")
        flash('Invalid login info', 'log')
        return redirect('/')
    print("*****************")
    session['uuid'] = user_in_db.id
    return redirect('/dashboard')

@app.route('/users/logout')
def logout():
    del session['uuid']
    return redirect('/')

