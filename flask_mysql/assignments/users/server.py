from flask import Flask, render_template, redirect, request

from users import User

app = Flask(__name__)
app.secret_key = 'dasjdsa'

@app.route('/')
def index():
    return render_template('add_user.html')

@app.route('/create_user', methods = ['POST'])
def create_user():
    data = {
        'fname':request.form['fname'],
        'lname':request.form['lname'],
        'email':request.form['email']
    }
    User.save(data)
    return redirect('/home')

@app.route('/home')
def users():
    users = User.get_all()
    return render_template('home.html', users = users)



if __name__ == '__main__':
    app.run (debug = True)