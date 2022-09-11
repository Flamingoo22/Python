from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from datetime import datetime
import math

class Message():
    def __init__(self, db_data):
        self.id = db_data['id']
        self.message = db_data['message']
        self.sender_id = db_data['user1_id']
        self.sender = db_data['sender']
        self.receiver_id = db_data['user2_id']
        self.receiver = db_data['receiver']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        
        
        
    def time_span(self):
        now = datetime.now()
        delta = now - self.created_at
        if delta.days > 0:
            return f'{delta.days} days ago'
        elif (math.floor(delta.total_seconds()/60)) >= 60:
            return f'{math.floor(math.floor(delta.total_seconds() /60)/60)} hours ago'
        elif delta.total_seconds() >= 60:
            return f'{math.floor(delta.total_seconds()/60)} minutes ago'
        else:
            return f'{math.floor(delta.total_seconds())} seconds ago'
        
    # def time_span(self):
    #     now = datetime.now()
    #     delta = now - self.created_at
    #     print(delta.days)
    #     print(delta.total_seconds())
    #     if delta.days > 0:
    #         return f"{delta.days} days ago"
    #     elif (math.floor(delta.total_seconds() / 60)) >= 60:
    #         return f"{math.floor(math.floor(delta.total_seconds() / 60)/60)} hours ago"
    #     elif delta.total_seconds() >= 60:
    #         return f"{math.floor(delta.total_seconds() / 60)} minutes ago"
    #     else:
    #         return f"{math.floor(delta.total_seconds())} seconds ago"
        
    @classmethod
    def my_message(cls, data):
        query = '''
                SELECT users.first_name as sender, users2.first_name AS receiver, messages.*
                FROM users
                LEFT JOIN messages
                ON users.id = messages.user1_id
                LEFT JOIN users AS users2
                ON messages.user2_id = users2.id
                WHERE users2.id = %(id)s;
                '''
        results = connectToMySQL(DATABASE).query_db(query, data)
        print(results)
        # if not results:
        #     return False
        print('***************')
        messages = []
        for message in results:
            messages.append(cls(message))
        return messages
    
    @classmethod
    def send(cls, data):
        query = '''
                INSERT INTO messages (message, user1_id, user2_id)
                VALUES(%(message)s,%(sender_id)s,%(receiver_id)s);
                '''
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def destroy(cls, data):
        query = '''
                DELETE FROM messages
                WHERE messages.id = %(id)s;
                '''
        return connectToMySQL(DATABASE).query_db(query, data)