from unittest import result
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja_model import Ninja

class Dojo():
    def __init__(self, db_data):
        self.id = db_data['id']
        self.name = db_data['name']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        
    @classmethod
    def create(cls, data):
        query = '''
                INSERT INTO dojos (name)
                VALUES (%(name)s);
                '''
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)
    
    @classmethod
    def get_my_ninjas(cls, data):
        query = '''
                SELECT * 
                FROM ninjas
                LEFT JOIN dojos
                ON ninjas.dojo_id = dojos.id
                WHERE dojos.id = %(id)s;
                '''
        results = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        ninjas = []
        # print('***********')
        # print(results)
        if len(results[0]) > 0:
            for ninja in results:
                ninjas.append(Ninja(ninja))
            return ninjas
        else:
            return False
    
    @classmethod
    def get_one(cls, data):
        query = '''
                SELECT * 
                FROM dojos
                WHERE dojos.id = %(id)s;
                '''
        result = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        print(result)
        if len(result) > 0:
            return cls(result[0])
        else:
            return False
        
    @classmethod
    def get_all(cls):
        query = '''
                SELECT * 
                FROM dojos;
                '''
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        dojos = []
        if len(results) > 0 :
            for dojo in results:
                dojos.append(cls(dojo))
            return dojos
        else:
            return False
        