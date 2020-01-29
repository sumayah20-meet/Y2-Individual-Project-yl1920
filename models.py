from sqlalchemy import Column,Integer,String,Date,Float,Boolean,DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
   __tablename__ = 'user '
   id = Column(Integer, primary_key=True)
   username = Column(String)
   password = Column(String)