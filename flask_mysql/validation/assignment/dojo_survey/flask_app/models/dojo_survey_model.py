from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Dojo:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.name = db_data['name']
        self.location = db_data['location']
        self.language = db_data['language']
        self.comment = db_data['comment']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        
    def __repr___(self):
        return f'id: {self.id} name:{self.name}'
    @classmethod
    def save(cls, data):
        query = '''
                INSERT INTO dojo_survey(name, location, language, comment)
                VALUES (%(name)s, %(location)s, %(language)s, %(comment)s);
                '''
        return connectToMySQL('dojo_survey').query_db( query, data)
    
    @classmethod
    def show_all(cls, data):
        query = '''
                SELECT *
                FROM dojo_survey
                WHERE dojo_survey.id = %(id)s
                '''
        results = connectToMySQL('dojo_survey').query_db(query, data)
        surveys = []
        for survey in results:
            surveys.append(cls(survey))
        return surveys
    
    @classmethod
    def choose_latest(cls):
        query = '''
                SELECT *
                FROM dojo_survey
                ORDER BY dojo_survey.id DESC
                '''
        results = connectToMySQL('dojo_survey').query_db(query)
        new_survey = cls(results[0])
        print(results[0])
        return new_survey
    
    @staticmethod
    def validate_survey(survey):
        is_valid = True
        if len(survey['name']) < 3:
            flash("Name is required.")
            is_valid = False
        return is_valid
