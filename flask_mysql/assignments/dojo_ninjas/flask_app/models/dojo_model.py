# We need to import the burger class from our models
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja_model, dojo_model

class Dojo:
    def __init__(self , db_data ):
        self.id = db_data['id']
        self.name = db_data['name']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        # We create a list so that later we can add in all the burgers that are associated with a dojo
        # to prevent mismatch of information self.ninjas = []  
    @classmethod
    def save( cls , data ):
        query = "INSERT INTO dojos ( name , created_at , updated_at ) VALUES (%(name)s,NOW(),NOW());"
        return connectToMySQL('dojos_and_ninjas').query_db( query, data)
    @classmethod
    def get_dojo_with_ninjas( cls , data ):
        query ='''
                SELECT * 
                FROM dojos 
                LEFT JOIN ninjas 
                ON ninjas.dojo_id = dojos.id 
                WHERE dojos.id = %(dojo_id)s;
                '''
        results = connectToMySQL('dojos_and_ninjas').query_db( query , data ) 
        print(results)
        dojo = cls( results[0] ) 
        dojo.ninjas = []  
        for row_from_db in results:
            ninja_data = {
                "id" : row_from_db["ninjas.id"],
                "dojo_id" : row_from_db["dojo_id"],
                "first_name" : row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "age" : row_from_db["age"], 
                "created_at" : row_from_db["ninjas.created_at"],
                "updated_at" : row_from_db["ninjas.updated_at"]
            }
            dojo.ninjas.append( ninja_model.Ninja( ninja_data ) )
        print( dojo )
        return dojo
    
    @classmethod
    def show_all(cls):
        query = 'SELECT * FROM dojos;' #DONT USE THAT, THIS RETURN DICTIONARY
        dojos_from_db = connectToMySQL('dojos_and_ninjas').query_db(query)
        dojos = []
        for dojo in dojos_from_db:
            dojos.append(cls(dojo))
        return dojos
    
    @classmethod
    def add(cls, data):
        query = 'INSERT INTO ninjas (dojo_id, first_name, last_name, created_at, updated_at) VALUES (%(dojo_id)s, %(fname)s, %(lname)s, NOW(), NOW()); '
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)


