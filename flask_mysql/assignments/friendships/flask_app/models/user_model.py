from flask_app.config.mysqlconnection import connectToMySQL


class User():
    def __init__(self,db_data):
        self.id = db_data['id']
        self.first_name = db_data['first_name']
        self.last_name = db_data['last_name']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        
    @classmethod
    def add(cls, data):
        query = '''
                INSERT INTO users(first_name, last_name)
                VALUES (%(first_name)s, %(last_name)s);
                '''
        return connectToMySQL('friendship').query_db(query, data)
    
    @classmethod
    def show_all_user(cls):
        query = '''
                SELECT *
                FROM users;
                '''
        results = connectToMySQL('friendship').query_db(query)
        if not results:
            return False
        users=[]
        for user_db in results:
            user = cls(user_db)
            users.append(user)
        return users
    
    @classmethod
    def show_all_friendship(cls):
        query = '''
                SELECT *
                FROM users
                LEFT JOIN friendships
                ON users.id = friendships.user_id
                LEFT JOIN users AS friend
                ON friendships.friend_id = friend.id;
                '''
        results = connectToMySQL('friendship').query_db(query)
        if not results:
            return False
        users = []
        for user_db in results:
            data = {
                'id':user_db['friend.id'],
                'first_name':user_db['friend.first_name'],
                'last_name':user_db['friend.last_name'],
                'created_at':user_db['friend.created_at'],
                'updated_at':user_db['friend.updated_at']
            }
            user = cls(user_db)
            friend = cls(data)
            user.friends = friend
            users.append(user)
        return users
    
    @classmethod
    def makefriends(cls, data):
        query = '''
                INSERT INTO friendships (user_id, friend_id)
                VALUES(%(user_id)s, %(friend_id)s);
                '''
        return connectToMySQL('friendship').query_db(query, data)
    
    @classmethod
    def destroy(cls, data):
        query = '''
                DELETE FROM friendships
                WHERE friendships.user_id = %(user_id)s AND friendships.friend_id = %(friend_id)s;
                '''
        return connectToMySQL('friendship').query_db(query, data)