from fcntl import F_SEAL_SEAL
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app, bcrypt
from flask import flash, session
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class User():
    def __init__(self, db_date):
        self.id = db_date['id']
        self.first_name = db_date['first_name']
        self.last_name = db_date['last_name']
        self.password = db_date['password']
        self.email = db_date['email']
        self.created_at = db_date['created_at']
        self.updated_at = db_date['updated_at']
        
    @classmethod
    def add(cls, data):
        query = '''
                INSERT INTO users (first_name, last_name, password, email)
                VALUES (%(fname)s, %(lname)s, %(password)s, %(email)s);
                '''
        return connectToMySQL('user_login').query_db(query, data)
        
    @classmethod
    def find_user_by_email(cls, data):
        query = '''
                SELECT *
                FROM users
                WHERE users.email = %(email)s;
                '''
        result = connectToMySQL('user_login').query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])
    
    @staticmethod
    def validate(user):
        is_valid = True
        if len(user['fname']) == 0:
            #err_tablename_tablecolumn
            flash('First Name is required.','err_users_first_name')
            is_valid = False
        if len(user['lname']) == 0:
            flash('Last Name is required.','err_users_last_name')
            is_valid = False
        if len(user['email']) < 3:
            flash('Email is required.', 'err_users_email')
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address!",'err_users_email')
            is_valid = False
        if len(user['password']) == 0:
            flash('Password is required.','err_users_password')
            is_valid = False
        if user['confirm_password'] != user["password"]:
            flash('Password do not match','err_users_confirm_password')
            is_valid = False
        return is_valid

    @staticmethod
    def validate_login(user):
        is_valid = True
        if len(user['email']) < 3:
            flash('Email is required.')
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address!")
            is_valid = False
        if len(user['password']) == 0:
            flash('Password is required.')
            is_valid = False
        if is_valid:
            potential_user = User.find_user_by_email({'email':user['email']})
            if not bcrypt.check_password_hash(potential_user.password, user['password']):
                flash('Incorrect Password')
                is_valid = False
            else:
                session['uuid'] = potential_user.id

            
        return is_valid