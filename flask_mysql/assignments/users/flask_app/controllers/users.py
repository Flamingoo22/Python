from flask_app import app
from flask import Flask, render_template, redirect, request

from flask_app.models.user import User


@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == "POST":
        data = {
        'fname':request.form['fname'],
        'lname':request.form['lname'],
        'email':request.form['email']
        }
        User.save(data)
        return redirect('/users')
    else:
        return render_template('add_user.html')

# @app.route('/create_user', methods = ['POST'])
# def create_user():

@app.route('/users')
def users():
    users = User.get_all()
    return render_template('home.html', users = users)

@app.route('/users/<int:user_id>')
def info(user_id):
    data = {
        'id': user_id
    }
    return render_template('user_info.html', user = User.get_one(data))

@app.route('/users/<int:user_id>/edit', methods = ['POST', 'GET'])
def edit(user_id):
    if request.method == 'POST':
        data = {
        'id': user_id,
        'fname':request.form['fname'],
        'lname':request.form['lname'],
        'email':request.form['email']
        }
        User.update(data)
        return redirect(f'/users')
    else:
        data = {
            'id': user_id
        }
        return render_template('edit_user.html', user = User.get_one(data))

@app.route('/delete/<int:user_id>')
def delete(user_id):
    data = {
        'id' : user_id,
    }
    User.delete(data)
    return redirect('/users')