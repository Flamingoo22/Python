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
    
    location = {
        "farm":(10,20),
        "cave":(5,10),
        "house":(2,5),
        "casino":(-50,50)
    }
    
    gold = random.randint(*location[request.form['name']])
    
    # farm = random.randint(10,20)
    # cave = random.randint(5,10)
    # house = random.randint(2,5)
    # casino = random.randint(-50,50)
    if 'gold' not in session:
        session["gold"] = 0
        session['display'] = [ ]
        session['name'] = request.form['name']
    
    session['gold'] += gold
    
    if gold > 0:
        session['display'].append(f'Earned {gold} golds from the {request.form["name"]}!  {x}')
    else:
        # session['gold'] += casino
        # if casino > 0:
        # session['display'].append(f'Entered a casino and won {casino} golds! CONGRAT!  {x}')
        session['display'].append(f'Entered a {request.form["name"]} and lost {gold} golds... Ouch..  {x}')
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