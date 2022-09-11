from flask_app import app
from flask_app.models.user_model import User
from flask import render_template, redirect, request

@app.route('/')
def dashboard():
    friendships = User.show_all_friendship()
    users = User.show_all_user()
    return render_template('dashboard.html', friendships= friendships, users = users)



'''
****************************
'''

@app.route('/add', methods = ['POST'])
def add():
    data = {
        **request.form
    }
    User.add(data)
    return redirect('/')

@app.route('/addfriend', methods = ['POST'])
def addfriend():
    data = {
        **request.form
    }
    if request.form['user_id'] == request.form['friend_id']:
        return redirect('/')
    friendship = User.show_all_friendship()
    for user in friendship:
        # print('*************************')
        # print(user.id)
        # print(request.form['user_id'])
        # print('*************************')
        if user.id == int(request.form['user_id']):    #request.form return a string and will not equal to the number
            # print('*************************')
            # print(user)
            # print('*************************')
            if user.friends.id == int(request.form['friend_id']):
                return redirect('/')
    User.makefriends(data)
    return redirect('/')

@app.route('/remove/<int:user_id>/<int:friend_id>')
def destroy(user_id, friend_id):
    data ={
        'user_id':user_id,
        'friend_id':friend_id
    }
    User.destroy(data)
    return redirect('/')