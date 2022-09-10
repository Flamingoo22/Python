from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author_model

class Book:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.title = db_data['title']
        self.num_page = db_data['num_page']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        
    @classmethod
    def save(cls, data):
        query = '''
                INSERT INTO books (title, num_page)
                VALUES (%(title)s, %(num_page)s);
                '''
        return connectToMySQL('books').query_db( query, data)
    
    @classmethod
    def get_book_favorite_author(cls, data):
        query = '''
                SELECT *
                FROM books
                LEFT JOIN fav_books
                ON books.id = fav_books.book_id
                LEFT JOIN authors
                ON fav_books.author_id = authors.id
                WHERE books.id = %(book_id)s;
                '''
        results = connectToMySQL('books').query_db(query, data)
        book_fav = cls( results[0] ) 
        book_fav.authors = []
        for row_from_db in results: 
            author_data = {
                'id' : row_from_db["authors.id"],
                'first_name' : row_from_db["first_name"],
                'last_name' : row_from_db["last_name"],
                'created_at' : row_from_db["authors.created_at"],
                'updated_at' : row_from_db["authors.updated_at"]
            }
            book_fav.authors.append(author_model.Author( author_data ))
        return book_fav
    
    @classmethod
    def get_books_not_favorited_author(cls, data):
        query = '''
                SELECT * FROM books, authors
                WHERE books.id = %(book_id)s 
                AND authors.id NOT IN (
                SELECT authors.id
                FROM books
                LEFT JOIN fav_books
                ON books.id = fav_books.book_id
                LEFT JOIN authors
                ON authors.id = fav_books.author_id
                WHERE books.id = %(book_id)s);
                '''
        results = connectToMySQL('books').query_db( query, data)
        if not results:  #IF NOT RESULTS/ RESOLVES ALL CONDITIONS
            # results = 'None'
            return False
        else:
            books_notfaved = cls(results[0])
            # books_notfaved = cls( results[0])
            books_notfaved.authors = []
            for row_from_db in results:
                author_data = {
                    'id' : row_from_db["authors.id"],
                    'first_name' : row_from_db["first_name"],
                    'last_name' : row_from_db["last_name"],
                    'created_at' : row_from_db["authors.created_at"],
                    'updated_at' : row_from_db["authors.updated_at"]
                }    #THIS CAN BE SKIP?
                books_notfaved.authors.append( author_model.Author(author_data) )
            return books_notfaved
    
    @classmethod
    def show_all_books(cls):
        query = 'SELECT * FROM books;'
        books_from_db = connectToMySQL('books').query_db(query)
        books = []
        for book in books_from_db:
            books.append(cls(book))
        return books
    
    @classmethod
    def add(cls, data):
        query = '''
                INSERT INTO books (title, num_page)
                VALUES (%(title)s, %(num_page)s);
                '''
        return connectToMySQL('books').query_db(query, data)
    
    
    @classmethod
    def show_one_book(cls, data):
        query = '''
                SELECT * 
                FROM books
                WHERE books.id = %(book_id)s;
                '''
        book_from_db = connectToMySQL('books').query_db(query, data)
        book = cls(book_from_db[0])
        return book
    
    @classmethod
    def add_fav_author(cls, data):
        query = '''
                INSERT INTO fav_books (book_id, author_id)
                VALUES (%(book_id)s,%(author_id)s);
                '''
        return connectToMySQL('books').query_db(query, data)