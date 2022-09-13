from flask import flash, session
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 



class User():
    def __init__(self, db_data):
        self.id = db_data['id']
        self.first_name =  db_data['first_name']
        self.last_name = db_data['last_name']
        self.email = db_data['email']
        self.password = db_data['password']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def create(cls,data):
        query = '''
                INSERT INTO users (first_name, last_name, email, password)
                VALUES (%(first_name)s, %(first_name)s, %(email)s, %(password)s);
                '''
        return connectToMySQL(DATABASE).query_db(query, data)
    
        
    @classmethod
    def show_all(cls):
        query = '''
                SELECT *
                FROM users
                '''
        results =  connectToMySQL(DATABASE).query_db(query)
        if not results:
            return False
        users = []
        for user_db in results:
            users.append(cls(user_db))
        return users
    
    @classmethod
    def show_one(cls, data):
        query = '''
                SELECT *
                FROM users
                WHERE users.id = %(id)s;
                '''
        result = connectToMySQL(DATABASE).query_db(query, data)
        if not result:
            return False
        user = cls(result[0])
        return user
    
    @classmethod
    def find_user_by_email(cls, data):
        query = '''
                SELECT *
                FROM users
                WHERE users.email = %(email)s;
                '''
        result = connectToMySQL(DATABASE).query_db(query, data)
        if not result:
            return False
        user = cls(result[0])
        return user
    
    @staticmethod
    def validate_register(data):
        is_valid = True
        if len(data['first_name']) <= 0:
            flash('first name cannot be empty','err_users_first_name')
            is_valid = False
        if len(data['last_name']) <= 0:
            flash('last name cannot be empty','err_users_last_name')
            is_valid = False
        if len(data['email']) <= 0:
            flash('email cannot be empty','err_users_email')
            is_valid = False
        elif not EMAIL_REGEX.match(data['email']):
            flash("Invalid email address!", 'err_users_invalid_email')
            is_valid = False
        elif User.find_user_by_email({'email':data['email']}):
            flash('email already existed','err_users_repeated_email')
            is_valid = False
        if len(data['password']) <= 0:
            flash('password cannot be empty','err_users_password')
            is_valid = False
        if not data['password'] == data['confirm_password']:
            flash('password doesnot match','err_users_confirm_password')
            is_valid = False
        return is_valid
    
    @staticmethod
    def validate_login(data):
        is_valid = True
        if len(data['email']) <= 0:
            flash('email cannot be empty', 'err_users_login_email')
            is_valid = False
        elif not EMAIL_REGEX.match(data['email']):
            flash("Invalid email address!", 'err_users_login_invalid_email')
            is_valid = False
        elif not User.find_user_by_email({'email':data['email']}):
            flash('email does not exist','err_users_login_not_exist_email')
            is_valid = False
        if len(data['pw']) <= 0:
            flash('password cannot be empty', 'err_users_login_password')
            is_valid = False
        if is_valid:
            potential_user = User.find_user_by_email({'email':data['email']})
            if not bcrypt.check_password_hash(potential_user.password, data['pw']):
                flash('Incorrect Password', 'err_users_login_invalid_password')
                is_valid = False
            else:
                session["uuid"] = potential_user.id
                session["username"] = potential_user.first_name
        return is_valid