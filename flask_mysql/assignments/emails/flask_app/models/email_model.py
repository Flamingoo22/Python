from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class Email():
    def __init__(self, db_database):
        self.id = db_database['id']
        self.email = db_database['email']
        self.created_at = db_database['created_at']
        self.updated_at = db_database['updated_at']     
        
    def __repre__(self):
        return f"id: {self.id}, email: {self.email}"
    
    @classmethod
    def save(cls, data):
        query = '''
                INSERT INTO emails (email)
                VALUES (%(email)s);
                '''
        return connectToMySQL('email').query_db(query, data)
        
    @classmethod
    def show_all(cls):
        query = '''
                SELECT *
                FROM emails
                '''
        results = connectToMySQL('email').query_db(query)
        emails = []
        for email in results:
            emails.append(cls(email))
        return emails
    
    @staticmethod
    def validate_email(emails, data):
        is_valid = True
        for email in data:
            if emails['email'] == email.email:
                flash("Email already existed")
                is_valid = False
                return is_valid
        if emails['email'] == '':
            flash('Email cannot be blank!')
            is_valid = False
        elif not EMAIL_REGEX.match(emails['email']):
            flash('Invalid email address!')
            is_valid = False
        return is_valid