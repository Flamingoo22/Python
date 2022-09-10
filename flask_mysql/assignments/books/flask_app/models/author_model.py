from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book_model

class Author:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.first_name = db_data['first_name']
        self.last_name = db_data['last_name']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        
    @classmethod
    def save(cls, data):
        query = '''
                INSERT INTO books (first_name, last_name)
                VALUES (%(first_name)s, %(last_name)s)
                '''
        return connectToMySQL('books').query_db( query, data)
    
    @classmethod
    def get_authors_favorited_books(cls, data):
        query = '''
                SELECT *
                FROM authors
                LEFT JOIN fav_books
                ON authors.id = fav_books.author_id
                LEFT JOIN books
                ON fav_books.book_id = books.id
                WHERE authors.id = %(id)s;
                '''
        results = connectToMySQL('books').query_db( query, data )
        author_fav = cls( results[0] )
        author_fav.books = []
        for row_from_db in results:
            book_data = {
                'id' : row_from_db["books.id"],
                'title' : row_from_db["title"],
                'num_page' : row_from_db["num_page"],
                'created_at' : row_from_db["books.created_at"],
                'updated_at' : row_from_db["books.updated_at"]
            }
            author_fav.books.append( book_model.Book(book_data) )
        return author_fav
    
    @classmethod
    def get_authors_not_favorited_book(cls, data):
        query = '''
                SELECT * FROM  authors, books
                WHERE authors.id= %(id)s AND books.id NOT IN (
                SELECT books.id
                FROM authors
                LEFT JOIN fav_books
                ON authors.id = fav_books.author_id
                LEFT JOIN books
                ON books.id = fav_books.book_id
                WHERE authors.id = %(id)s);
                '''
        results = connectToMySQL('books').query_db( query, data)
        print('THIS IS A COMMENT***************')
        print(results) 
        if results[0] == None:
            author_notfaved = 0
        else:
            author_notfaved = cls(results[0])
        author_notfaved.books = []
        for row_from_db in results:
            book_data = {
                'id' : row_from_db["books.id"],
                'title' : row_from_db["title"],
                'num_page' : row_from_db["num_page"],
                'created_at' : row_from_db["books.created_at"],
                'updated_at' : row_from_db["books.updated_at"]
            }
            author_notfaved.books.append( book_model.Book(book_data) )
        return author_notfaved
    
    @classmethod
    def show_all_authors(cls):
        query = 'SELECT * FROM authors;'
        authors_from_db = connectToMySQL('books').query_db(query)
        authors = []
        # print(authors)
        for author in authors_from_db:
            authors.append(cls(author))
        print(authors)
        return authors
    
    @classmethod
    def add(cls, data):
        query = '''
                INSERT INTO books (first_name, last_name)
                VALUES (%(fname)s, %(lname)s);
                '''
        return connectToMySQL('books').query_db(query, data)


    @classmethod
    def show_one_author(cls, data):
        query = '''
                SELECT * 
                FROM books.authors
                WHERE authors.id = %(id)s;
                '''
        author_from_db = connectToMySQL('books').query_db(query, data)
        author = cls(author_from_db[0])
        return author
    
    @classmethod
    def add_fav_book(cls, data):
        query = '''
                INSERT INTO fav_books (book_id, author_id)
                VALUES (%(book_id)s, %(author_id)s);
                '''
        return connectToMySQL('books').query_db(query, data)