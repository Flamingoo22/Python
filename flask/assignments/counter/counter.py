from cmath import isnan
from errno import ESTALE
from flask import Flask, render_template, request, redirect, session,url_for

app = Flask(__name__)
app.secret_key = "dsakjd"


@app.route("/")
def entry_counter():
    if 'btn1' in session:
            session['btn1'] += 1
    else:
        session["btn1"] = 1
    return render_template("index.html")

@app.route('/counter')
def num_counter():
    if "num" in session:
        if'increment' in session:
            session['num'] += int(session['increment'])
        else:
            session['num'] += 1
    else:
        session["num"] = 1
    return redirect('/')


@app.route('/increment', methods=['POST'])
def increment():
    if request.form['increment'] == "":    #to prevent server error if user input a sp ace
        return redirect('/')
    else:
        session['increment'] = request.form['increment']  #if user provides an integer, we will retreive the information
        # print(f"your increment number is {session['increment']}")
        return redirect('/')

# once we learn database, the information will be send to query

@app.route('/reset')
def reset():
    session.clear()
    return redirect("/")


if __name__=="__main__":
    app.run(debug=True)
    
# reorganize the file, open from folder instead of the entire file