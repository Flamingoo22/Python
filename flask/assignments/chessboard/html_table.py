from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def names():
    users = [
    {'first_name' : 'Michael', 'last_name' : 'Choi','full_name' : 'Micahel Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin','full_name':'John Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen','full_name':'Mark Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel', 'full_name':'KB Tonel'}
    ]
    return render_template("html_table.html", users=users)






if __name__=="__main__":
    app.run(debug=True)