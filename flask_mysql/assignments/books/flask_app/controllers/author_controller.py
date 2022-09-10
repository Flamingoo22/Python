from flask_app import app
from flask import Flask, render_template, redirect, request

from flask_app.models.author_model import Author


@app.route('/authors/<int:author_id>')
def authors_show(author_id):
    data = {
        'id': author_id
    }
    return render_template('authors_show.html', fav = Author.get_authors_favorited_books(data), notfav = Author.get_authors_not_favorited_book(data), author = Author.show_one_author(data))



'''
*********************************************************
ACTION ROUTES DOWN
*********************************************************
'''


@app.route('/authors/addbook', methods = ['POST'])
def author_addbook():
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    author_id = request.form['author_id']
    Author.add_fav_book(data)
    return redirect(f'/authors/{author_id}')


@app.route('/authors', methods=['GET','POST'])
def authors():
    if request.method == 'POST':
        data = {
            'first_name': request.form['fname'],
            'last_name': request.form['lname']
        }
        Author.save(data)
        return redirect('/authors')
    else:
        authors = Author.show_all_authors()
        return render_template('authors.html', authors = authors)