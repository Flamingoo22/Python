from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.email_model import Email

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/validate', methods=['POST'])
def validate():
    if not Email.validate_email(request.form, Email.show_all()):
        return redirect('/')
    else:
        Email.save(request.form)
        return redirect('/success')

@app.route('/success')
def display():
    emails = Email.show_all()
    return render_template('success.html', emails = emails)