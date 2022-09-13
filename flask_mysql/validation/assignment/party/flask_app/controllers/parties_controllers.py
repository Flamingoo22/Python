from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_app.models.users_model import User
from flask_app.models.party_model import Party

@app.route('/parties/new')
def new_party_form():
    if 'uuid' not in session:
        return redirect('/')
    return render_template('parties_new.html')












'''
****************ACTION ROUTE********************
'''


@app.route('/parties/create', methods = ['POST'])
def process_party():
    if 'uuid' not in session:
        return redirect('/')
    if not Party.validate(request.form):
        return redirect('/parties/new')
    data = {
        **request.form,
        'user_id':session['uuid']
    }
    Party.create(data)
    return redirect('/dashboard')

@app.route('/parties/<int:id>/delete')
def del_party(id):
    if 'uuid' not in session:
        return redirect('/')
    if not int(session['uuid']) == id:
        flash("Whoa there, that's not yours, hands off!")
        return redirect('/dashboard')
    Party.delete({'id':id})
    return redirect('/dashboard')

@app.route('/parties/<int:id>/edit')
def edit_party(id):
    if 'uuid' not in session:
        return redirect('/')
    if not int(session['uuid']) == id:
        flash("Whoa there, that's not yours, hands off!")
        return redirect('/dashboard')
    party = Party.get_by_id({'id':id})
    return render_template('parties_edit.html', party = party)