from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, Book

app = Flask(__name__)

engine = create_engine('sqlite:///webshop.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
db = DBSession()

@app.route("/")
def index():
    return "Hello World!"

@app.route("/list")
def list():
    books = db.query(Book).all()
    return render_template('list.html', books=books)

@app.route("/new", methods=['GET', 'POST'])
def newBook():
    return render_template('new.html')

@app.route("/edit/<int:id>", methods=['GET', 'POST'])
def editBook(id):
    return render_template('edit.html', id=id)

@app.route("/delete/<int:id>", methods=['GET', 'POST'])
def deleteBook(id):
    return render_template('delete.html', id=id)


if __name__ == "__main__":
    app.run(debug=True)