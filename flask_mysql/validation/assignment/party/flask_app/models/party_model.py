from flask import flash

from flask_app.models.users_model import User
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Party:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.what = db_data['what']
        self.location = db_data['location']
        self.all_ages = db_data['all_ages']
        self.description = db_data['description']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.user_id = db_data['user_id']
        
    @classmethod
    def create(cls,data):
        query = '''
                INSERT INTO parties(what, location,all_ages,description, user_id)
                VALUES (%(what)s, %(location)s, %(all_ages)s, %(description)s, %(user_id)s);
                '''
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def get_by_id(cls,data):
        query = '''
                SELECT *
                FROM parties
                WHERE parties.id = %(id)s;
                '''
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return False
        return cls(results[0])
    
    
    
    @classmethod
    def get_all(cls):
        query = '''
                SELECT *
                FROM parties
                LEFT JOIN users
                ON parties.user_id = users.id
                '''
        results = connectToMySQL(DATABASE).query_db(query)
        if not results:
            return []
        all_parties = []
        for row in results:
            this_party = cls(row)
            user_data = {
                **row,
                'id':row['users.id'],
                'created_at':row['created_at'],
                'updated_at':row['updated_at']
            }
            this_user = User(user_data)
            this_party.palnner = this_user
            all_parties.append(this_party)
        return all_parties
    
    @classmethod
    def delete(cls, data):
        query = '''
                DELETE FROM parties
                WHERE parties.id = %(id)s;
                '''
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @staticmethod
    def validate(form_data):
        is_valid = True
        if len(form_data['what'])<1:
            flash('What is required')
            is_valid = False
        is_valid = True
        if len(form_data['location'])<1:
            flash('Location is required')
            is_valid = False
        is_valid = True
        if len(form_data['date'])<1:
            flash('Date is required')
            is_valid = False
        is_valid = True
        if len(form_data['description'])<1:
            flash('Description is required')
            is_valid = False
        if 'all_ages' not in form_data:
            flash('all ages required')
            is_valid = False
        return is_valid