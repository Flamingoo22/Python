from turtle import color
from flask import Flask, render_template, redirect  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return render_template("index.html", phrase='hello', times=5)             # Return the string 'Hello World!' as a response

# @app.route('/success')
# def success():
#     return "success"

# @app.route('/users/<username>/<id>')
# def show_user_profile(username, id):
#     print(username)
#     print(id)
#     return "username: " + username + ", id: " + id

# import statements, maybe some other routes
@app.route("/dojo")
def dojo():
    return "Dojo!"

@app.route("/say/<string:val>")
def say(val):
    return f"Hi {val}"

@app.route("/repeat/<int:num>/<string:val>")
def repeat(num,val):
    return val * num

# 
# def play(x):
#     return render_template("index.html", x=x, color=color)

@app.route("/play")
@app.route("/play/<int:x>")
@app.route("/play/<int:x>/<color>")  #path variable <>
def play(x=3,color="rgb(2,254,254)"):
    return render_template("index.html", x=x, color=color)


@app.route("/gg")
def gg():
    return "Sorry No Page Found"

@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again.",404

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.





