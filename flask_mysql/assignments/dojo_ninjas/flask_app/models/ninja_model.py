from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.dojo_id = data['dojo_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM ninjas;'
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        ninjas = []
        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas
    
    @classmethod
    def save (cls, data ):
        query = 'INSERT INTO ninjas (dojo_id, first_name, last_name, age, created_at, updated_at) VALUES (%(dojo_id)s, %(fname)s, %(lname)s, %(age)s, NOW(), NOW() ); '
        return connectToMySQL('dojos_and_ninjas').query_db( query, data )
    
    @classmethod
    def delete(cls,data):
        query = 'DELETE FROM ninjas WHERE ninjas.id = %(id)s;'
        return connectToMySQL('ninjas').query_db( query, data )

    @classmethod
    def update(cls,data):
        query = 'UPDATE ninjas SET first_name = %(fname)s, last_name = %(lname)s, age = %(age)s, updated_at = NOW() WHERE ninjas.id = %(id)s;'
        return connectToMySQL('ninjas').query_db( query, data )
    
    @classmethod
    def get_one(cls, data):
        query = 'SELECT * FROM ninjas WHERE ninjas.id = %(id)s;'
        ninja_from_db = connectToMySQL('ninjas').query_db(query, data)
        if ninja_from_db:
            return cls(ninja_from_db[0])