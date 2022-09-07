from flask_app import app
from flask import Flask, render_template, redirect, request

from flask_app.models.ninja_model import Ninja
from flask_app.models.dojo_model import Dojo





@app.route('/dojos', methods = ['GET', 'POST'])
def dojos():
    if request.method == 'POST':
        data = {
            'name':request.form['name']
        }
        Dojo.save(data)
        return redirect('/dojos')
    else:
        dojos = Dojo.show_all()
        return render_template('dojos.html', dojos = dojos)


@app.route('/ninjas', methods = ['GET', 'POST'])
def new_ninja():
    if request.method == 'POST':
        data = {
        'dojo_id':request.form['dojo'],
        'fname':request.form['fname'],
        'lname':request.form['lname'],
        'age':request.form['age']
        }
        Ninja.save(data)
        return redirect ('/dojos')
    else:
        dojos = Dojo.show_all()
    return render_template('new_ninja.html', dojos = dojos)



@app.route('/dojos/<dojo_id>')
def dojo_show(dojo_id):
    data = {
        'dojo_id': dojo_id
    }
    return render_template('dojo_show.html', dojo = Dojo.get_dojo_with_ninjas(data))
