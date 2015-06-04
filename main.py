from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, Book

import random, string

app = Flask(__name__)

engine = create_engine('sqlite:///webshop.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
db = DBSession()

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/list")
def list():
    books = db.query(Book).order_by(Book.id.desc()).all()
    return render_template('list.html', books=books)

@app.route("/new", methods=['GET', 'POST'])
def newBook():
    if request.method == 'POST':
        newBook = Book()
        newBook.title = request.form['title']
        newBook.author = request.form['author']
        newBook.price = request.form['price']
        newBook.description = request.form['description']
        db.add(newBook)
        db.commit()
        flash(newBook.title + ' book created!')
        return redirect(url_for('list'))
    return render_template('new.html')

@app.route("/edit/<int:id>", methods=['GET', 'POST'])
def editBook(id):
    book = db.query(Book).filter_by(id=id).one()
    if request.method == 'POST':
        book.title = request.form['title']
        book.author = request.form['author']
        book.price = request.form['price']
        book.description = request.form['description']
        db.add(book)
        db.commit()
        return redirect(url_for('list'))
    return render_template('edit.html', book=book)

@app.route("/delete/<int:id>", methods=['GET', 'POST'])
def deleteBook(id):
    book = db.query(Book).filter_by(id=id).one()
    if request.method == 'POST':
        db.delete(book)
        db.commit()
        flash('You have deleted ' + book.title)
        return redirect(url_for('list'))
    return render_template('delete.html', book=book)

@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html')

if __name__ == "__main__":
    app.secret_key = 'dlkjal34324kjh2l3k4h'
    app.run(debug=True)