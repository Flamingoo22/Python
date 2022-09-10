from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import recipe_model
from flask import flash, session
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User():
    def __init__(self, db_date):
        self.id = db_date['id']
        self.first_name = db_date['first_name']
        self.last_name = db_date['last_name']
        self.email = db_date['email']
        self.password = db_date['password']
        self.created_at = db_date['created_at']
        self.updated_at = db_date['updated_at']
        
    @classmethod
    def add(cls, data):
        query = '''
                INSERT users(first_name, last_name, email, password)
                VALUES(%(first_name)s,%(last_name)s,%(email)s,%(password)s);
                '''
        return connectToMySQL('recipe').query_db(query, data)
    
    @classmethod
    def find_user_by_email(cls, data):
        query = '''
                SELECT *
                FROM users
                WHERE users.email = %(email)s;
                '''
        result = connectToMySQL('recipe').query_db(query, data)
        if not result:
            return False
        return cls(result[0])
    
    @classmethod
    def show_all(cls, data):
        query = '''
                SELECT *
                FROM users
                LEFT JOIN ;
                '''
        results = connectToMySQL('recipe').query_db(query, data)
        users = []
        if results:
            for row_data in results:
                users.append(cls(row_data))
            return users
        else:
            return False
        
    @classmethod
    def show_one(cls,data):
        query = '''
                SELECT *
                FROM users
                WHERE users.id = %(id)s;
                '''
        results = connectToMySQL('recipe').query_db(query, data)
        if results:
            user = cls(results[0])
            return user
        else:
            return False
        
    @classmethod
    def show_user_recipe(cls, data):
        query = '''
                SELECT *
                FROM users
                LEFT JOIN share_recipe
                ON users.id = share_recipe.user_id
                LEFT JOIN recipes
                ON share_recipe.recipe_id = recipes.id
                WHERE users.id = %(id)s;
                '''
        results = connectToMySQL('recipe').query_db(query, data)
        if results:
            user_all_recipes = []
            for recipe in results:
                user = cls(recipe)
                recipe_data = {
                    **recipe,
                    "id":recipe['recipes.id'],
                    'created_at':recipe['recipes.created_at'],
                    'updated_at':recipe['recipes.updated_at']
                }
                recipe_instance = recipe_model.Recipe(recipe_data)
                user.recipes = recipe_instance
                user_all_recipes.append(user)
            return user_all_recipes
        else:
            return False

    @staticmethod
    def validate_register(user):
        is_valid = True
        if len(user['fname']) == 0:
            flash('First Name is required.')
            is_valid = False
        if len(user['lname']) == 0:
            flash('Last Name is required.')
            is_valid = False
        if len(user['email']) < 3:
            flash('Email is required.')
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address!")
            is_valid = False
        if len(user['password']) == 0:
            flash('Password is required.')
            is_valid = False
        if user['confirm_password'] != user["password"]:
            flash('Password do not match')
            is_valid = False
        return is_valid
    
    @staticmethod
    def validate_login(user):
        is_valid = True
        if len(user['email']) < 3:
            flash('Email is required.')
            is_valid = False
        elif not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address!")
            is_valid = False
        if len(user['pw']) <= 0:
            flash('Password is required.')
            is_valid = False
        if is_valid:
            if not User.find_user_by_email({'email':user['email']}):
                flash("Invalid email address!")
                is_valid = False
            else: 
                potential_user = User.find_user_by_email({'email':user['email']})
                if not bcrypt.check_password_hash(potential_user.password, user['pw']):
                    flash('Incorrect Password')
                    is_valid = False
                else:
                    session["uuid"] = potential_user.id
                
        return is_valid

