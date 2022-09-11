from flask import render_template, redirect, session, flash, request
from flask_app import app
from flask_app.models.message_model import Message

@app.route('/message/send', methods = ['POST'])
def send_message():
    if 'uuid' not in session:
        return ('/')
    data = {
        'message': request.form['message'],
        'sender_id': request.form['sender_id'],
        'receiver_id': request.form['receiver_id']
        
    }
    
    Message.send(data)
    return redirect('/dashboard')

@app.route('/message/delete/<int:id>')
def destroy(id):
    if 'uuid' not in session:
        return ('/')
    data = {
        'id':id
    }
    Message.destroy(data)
    return redirect('/dashboard')