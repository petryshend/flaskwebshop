import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, Text, Numeric, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    author = Column(String(255), nullable=True)
    description = Column(Text(), nullable=True)
    price = Column(Numeric(), nullable=True)
    created = Column(DateTime(), default=datetime.datetime.utcnow)

engine = create_engine('sqlite:///webshop.db')

Base.metadata.create_all(engine)