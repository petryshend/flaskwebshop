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

    return render_template('list.html')


if __name__ == "__main__":
    app.run(debug=True)