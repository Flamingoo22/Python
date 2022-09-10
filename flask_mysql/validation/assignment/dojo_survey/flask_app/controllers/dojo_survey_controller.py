from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo_survey_model import Dojo

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/info', methods=['POST'])
def collect_info():
    if not Dojo.validate_survey(request.form):
        return redirect('/')
    else:
        data = {
            'name':request.form['name'],
            'location':request.form['dojo_location'],
            'language':request.form['fav_language'],
            'comment':request.form['comment']
        }
        Dojo.save(data)
        return redirect('/result')


@app.route('/result')
def return_home():
    dojos = Dojo.choose_latest()
    return render_template('show.html', survey = dojos)
