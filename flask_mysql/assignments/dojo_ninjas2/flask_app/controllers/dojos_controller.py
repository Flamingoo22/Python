from flask_app import app
from flask import render_template, redirect, request

from flask_app.models.dojo_model import Dojo

@app.route('/')
def dojos():
    dojos = Dojo.get_all()
    return render_template('dojos.html', dojos = dojos)

@app.route('/create', methods=['POST'])
def create():
    data = {
        'name': request.form['name']
    }
    Dojo.create(data)
    return redirect('/')

@app.route('/<int:dojo_id>')
def show_one(dojo_id):
    data = {
        'id':dojo_id
    }
    ninjas = Dojo.get_my_ninjas(data)
    dojo = Dojo.get_one(data)
    # print('**********')
    # # print(dojo)
    # print(ninjas)
    # print('**********')
    return render_template('dojo.html', ninjas = ninjas, dojo = dojo)

@app.route('/add_ninja')
def add_ninja():
    dojos = Dojo.get_all()
    return render_template('new_ninja.html', dojos = dojos)