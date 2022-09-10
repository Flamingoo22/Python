from flask_app.config.mysqlconnection import connectToMySQL

class Ninja():
    def __init__(self, db_data):
        self.id = db_data['id']
        self.dojo_id = db_data['dojo_id']
        self.first_name = db_data['first_name']
        self.last_name = db_data['last_name']
        self.age = db_data['age']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        
    def __repr__(self):
        return f'id:{self.id}, first_name:{self.first_name}, last_name:{self.last_name}'
    
    @classmethod
    def create(cls , data):
        query = '''
                INSERT INTO ninjas (dojo_id, first_name, last_name, age)  
                VALUES (%(id)s, %(fname)s, %(lname)s, %(age)s);
                '''
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)