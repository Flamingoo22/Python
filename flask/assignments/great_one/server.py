from flask import Flask, render_template, request, redirect, session, url_for
import random

app = Flask(__name__)
app.secret_key = 'dasdad'


@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        if 'random' in session:                             #test if random number is in the session
            pass                                            #if we already have a random number, move on
        else:
            session['random']=random.randint(1,100)         #if not, create one
            print(session['random'])                        #cheating answer
        session['number']= request.form['number']           #get the guess answer
        if int(session['number']) > session['random']:      #if answer is too big, print too BIGGG
            session.pop('number')
            result = "TOO BIG!!"
        elif int(session['number']) < session['random']:    #if guess is small, print too smalll
            session.pop('number')
            result = "TOO SMALL!!"
        else:
            # session.clear()                                 #guess correctly, restart
            result = 'Correct!'
        
        return render_template("index.html", result=result)
    else:
        return render_template("index.html")

# @app.route('/testing')
# def compare():
#     return redirect('/')                                  #prove of getting stuck for 2 hours



if __name__ == "__main__":
    app.run(debug=True)