from flask import Flask, render_template, request, redirect
from datetime import date
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    time = date.today()
    count_straw = request.form['strawberry']
    count_rasp = request.form['raspberry']
    count_apple = request.form['apple']
    last_name = request.form['first_name']
    first_name = request.form['last_name']
    id = request.form['student_id']
    count = int(count_rasp)+int(count_apple)+int(count_straw)
    return render_template("checkout.html", strawberry=count_straw, raspberry=count_rasp, apple=count_apple, last_name=last_name, first_name=first_name, count=count, id=id, time=time)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    