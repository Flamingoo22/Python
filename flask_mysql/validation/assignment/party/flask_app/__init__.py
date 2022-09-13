from flask import Flask
DATABASE = 'party'
from flask_bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = 'dsadsadsa'