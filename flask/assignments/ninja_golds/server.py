from flask import Flask, redirect, session, render_template, request
import random

app = Flask(__name__)
app.secret_key = "djksajlkdsa"



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    farm = random.randint(10,20)
    cave = random.randint(5,10)
    house = random.randint(2,5)
    casino = random.randint(-50,50)
    if 'display' and 'gold' in session:
        # if 'gold' in session:
        session['name'] = request.form['name']
        session.pop('name')
        session['name'] = request.form['name']
        print(session['name'])
        # print(session['display'])
        if session['name'] == 'farm':
            session['gold'] += farm
            session['display'].append(f'Earned {farm} golds from the {session["name"]}!')
            print(farm)
        elif session['name'] == 'cave':
            session['gold'] += cave
            session['display'].append(f'Earned {cave} golds from the {session["name"]}!')
            print(cave)
        elif session['name'] == 'house':
            session['gold'] += house
            print(house)
            session['display'].append(f'Earned {house} golds from the {session["name"]}!')
        else:
            session['gold'] += casino
            if casino > 0:
                session['display'].append(f'Entered a casino and won {casino} golds! CONGRAT!')
            else:
                session['display'].append(f'Entered a casino and lost {casino} golds... Ouch..')
            # print(casino)
    else: 
        session["gold"] = 0
        session['display'] = [ ]
    # else:
        
    return redirect('/')


if __name__ == "__main__":
    app.run(debug = True)