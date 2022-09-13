from flask import Flask
from flask_bcrypt import Bcrypt
DATABASE = 'private_wall'

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = 'dsadsa'