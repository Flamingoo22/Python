from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = "dsa"

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/info', methods=['POST'])
def collect_info():
    session['name'] = request.form['name']
    session['location'] = request.form['dojo_location']
    session['language'] = request.form['fav_language']
    session['comment'] = request.form['comment']
    session['rate'] = request.form['rate']
    session['consent'] = "User favorite language is Python!"
    return redirect('/show')

@app.route('/show')
def return_home():
    return render_template('show.html')

if __name__ == "__main__":
    app.run(debug=True)