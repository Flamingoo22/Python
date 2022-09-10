from flask_app import app
from flask import render_template, redirect, request

from flask_app.models.ninja_model import Ninja

@app.route('/ninja', methods=['POST'])
def add():
    # data = {
    # 'id':request.form['dojo_id'],
    # 'fname':request.form['fname'],
    # 'lname':request.form['lname'],
    # 'age':request.form['age']
    # }
    Ninja.create(request.form)
    return redirect('/')