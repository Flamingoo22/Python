from flask import Flask, redirect, session, render_template, request
import random
import datetime

app = Flask(__name__)
app.secret_key = "djksajlkdsa"



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    time = datetime.datetime.now()
    x = time.strftime("%x %X")
    farm = random.randint(10,20)
    cave = random.randint(5,10)
    house = random.randint(2,5)
    casino = random.randint(-50,50)
    if 'display' and 'gold' in session:
        session['name'] = request.form['name']
        session.pop('name')
        session['name'] = request.form['name']
        print(session['name'])
    else:
        session["gold"] = 0
        session['display'] = [ ]
        session['name'] = request.form['name']
    if session['name'] == 'farm':
        session['gold'] += farm
        session['display'].append(f'Earned {farm} golds from the {session["name"]}!  {x}')
        print(farm)
    elif session['name'] == 'cave':
        session['gold'] += cave
        session['display'].append(f'Earned {cave} golds from the {session["name"]}!  {x}')
        print(cave)
    elif session['name'] == 'house':
        session['gold'] += house
        print(house)
        session['display'].append(f'Earned {house} golds from the {session["name"]}!  {x}')
    else:
        session['gold'] += casino
        if casino > 0:
            session['display'].append(f'Entered a casino and won {casino} golds! CONGRAT!  {x}')
        else:
            session['display'].append(f'Entered a casino and lost {casino} golds... Ouch..  {x}')
        # print(casino)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug = True)
    
    
    
# FOR THE BONUSES
# SENSEI BONUS: Have the activities display in descending order, with the most recent activity first
# let variable start at the length and decrement.

# SENSEI BONUS: Provide winning parameters to the game--for example, a user must obtain 500 gold in less than 15 moves. Only display the reset button once the user has won or lost.
# add a count everytime page is re-enter count+1; and set if conditions inside the index.html file if the count reached 15 the failure page will pop

# SENSEI BONUS: Complete the "/process_money" route without 4 conditional statements (i.e. without doing if farm...elif cave...etc.)
# Not sure about this... Ask Spencer on Tuesday