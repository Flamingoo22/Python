from flask import Flask, render_template, request, redirect, session, url_for
import random

app = Flask(__name__)
app.secret_key = 'dasdad'


@app.route('/', methods=['GET','POST'])
def index():
    # else:
    if 'result' in session:
        result = session['result']
        return render_template("index.html",result=result)
    else:
        return render_template('index.html',result='')

@app.route('/testing', methods=["POST"])
def compare():
    # if request.method == 'POST':
        if 'random' in session:                             #test if random number is in the session
            pass                                            #if we already have a random number, move on
        else:
            session['random']=random.randint(1,100)         #if not, create one
            print(session['random'])                        #cheating answer
        session['number']= request.form['number']           #get the guess answer
        if int(session['number']) > session['random']:      #if answer is too big, print too BIGGG
            session.pop('number')
            session['result'] = "TOO BIG!!"
        elif int(session['number']) < session['random']:    #if guess is small, print too smalll
            session.pop('number')
            session['result'] = "TOO LOW!!"
        else:
            # session.clear()                                 #guess correctly, restart
            session['result'] = 'Correct!'
        return redirect("/")
    # return redirect('/')                                  # getting stuck for 2 hours 

@app.route('/again')
def clear():
    session.clear()
    session['random']=random.randint(1,100)         #if not, create one
    print(session['random'])       
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)