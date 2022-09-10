from flask_app import app
from flask import Flask, render_template, redirect, request

from flask_app.models.sample_model import Sample





@app.route('/dojos', methods = ['GET', 'POST'])
def dojos():
    if request.method == 'POST':
        data = {
            'name':request.form['name']
        }
        Sample.save(data)
        return redirect('/dojos')
    else:
        dojos = Sample.show_all()
        return render_template('sample.html')


@app.route('/ninjas', methods = ['GET', 'POST'])
def new_ninja():
    if request.method == 'POST':
        data = {
        'dojo_id':request.form['dojo'],
        'fname':request.form['fname'],
        'lname':request.form['lname'],
        'age':request.form['age']
        }
        Sample.save(data)
        return redirect ('/')
    else:
        sample = Sample.show_all()
    return render_template('.html')



@app.route('/')
def dojo_show():
    return render_template('.html')
