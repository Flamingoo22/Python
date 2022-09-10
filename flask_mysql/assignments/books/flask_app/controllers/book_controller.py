from flask_app import app
from flask import Flask, render_template, redirect, request

from flask_app.models.book_model import Book

@app.route('/')
def redi():
    return redirect('/books')



@app.route('/books/<int:book_id>')
def books_show(book_id):
    data = {
        'book_id': book_id
    }
    context = {
        "notfav":Book.get_books_not_favorited_author(data),
        'fav':Book.get_book_favorite_author(data),
        'books':Book.show_one_book(data)
    }
    return render_template('books_show.html', **context)




'''
*********************************************************
ACTION ROUTES DOWN
*********************************************************
'''



@app.route('/books', methods=['GET','POST'])
def books():
    if request.method == 'POST':
        data = {
            'title': request.form['title'],
            'num_page': request.form['npage']
        }
        Book.save(data)
        return redirect('/books')
    else:
        books = Book.show_all_books()
        return render_template('books.html', books = books)
    
    
    
@app.route('/books/addauthor', methods = ['POST'])
def book_addauthor():
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    book_id = request.form['author_id']
    Book.add_fav_book(data)
    return redirect(f'/books/{book_id}')