from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self,db_data):
        self.id = db_data['id']
        self.first_name = db_data['first_name']
        self.last_name = db_data['last_name']
        self.password = db_data['password']
        self.email = db_data['email']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        
    @classmethod
    def create(cls, data):
        query = '''
                INSERT INTO users(first_name,last_name,password,email)
                VALUES(%(first_name)s, %(last_name)s, %(password)s, %(email)s);
                '''
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def get_by_email(cls,data):
        query = '''
                SELECT *
                FROM users
                WHERE users.email = %(email)s;
                '''
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return False
        return cls(results[0])
    
    @classmethod
    def get_by_id(cls,data):
        query = '''
                SELECT *
                FROM users
                WHERE users.id = %(id)s;
                '''
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return False
        return cls(results[0])
    
    @staticmethod
    def validate(user_data):
        is_valid = True
        if len(user_data['first_name']) < 1:
            flash('First name required', 'reg')
            is_valid = False
        if len(user_data['last_name']) < 1:
            flash('Last name required', 'reg')
            is_valid = False
        if len(user_data['email']) < 1:
            flash('Email required', 'reg')
            is_valid = False
        elif not EMAIL_REGEX.match(user_data['email']):
            flash('Invalid Email format','reg')
            is_valid = False
        else: 
            data = {
                'email':user_data['email']
            }
            potential_user = User.get_by_email(data)
            if potential_user:
                flash('email already registered','reg')
        print(is_valid)
        if len(user_data['password']) < 0:
            flash('First name required', 'reg')
            is_valid = False
        elif not user_data['password'] == user_data['confirm_password']:
            flash("Password don't match",'reg')
            is_valid = False
        print(is_valid)
        return is_valid