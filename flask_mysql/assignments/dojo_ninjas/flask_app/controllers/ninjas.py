from flask_app import app
from flask import Flask, render_template, redirect, request

from flask_app.models.ninja import Ninja


@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == "POST":
        data = {
        'fname':request.form['fname'],
        'lname':request.form['lname'],
        'age':request.form['age']
        }
        Ninja.save(data)
        return redirect('/')
    else:
        return render_template('')

# @app.route('/create_user', methods = ['POST'])
# def create_user():

@app.route('/users')
def users():
    ninjas = Ninja.get_all()
    return render_template('', ninjas = ninjas)

@app.route('/users/<int:user_id>')
def info(ninja_id):
    data = {
        'id': ninja_id
    }
    return render_template('', ninja = Ninja.get_one(data))

@app.route('/users/<int:user_id>/edit', methods = ['POST', 'GET'])
def edit(ninja_id):
    if request.method == 'POST':
        data = {
        'id': ninja_id,
        'fname':request.form['fname'],
        'lname':request.form['lname'],
        'age':request.form['age']
        }
        Ninja.update(data)
        return redirect(f'/users')
    else:
        data = {
            'id': ninja_id
        }
        return render_template('', ninja = Ninja.get_one(data))

@app.route('/delete/<int:user_id>')
def delete(ninja_id):
    data = {
        'id' : ninja_id,
    }
    Ninja.delete(data)
    return redirect('/users')