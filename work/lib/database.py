from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sqlalchemy
import sqlalchemy.ext.declarative
from sqlalchemy import desc

import datetime

#import logging
 
#logging.basicConfig()
#logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

engine = create_engine('mysql://root:password@db/loto?charset=utf8')

Session = sessionmaker(bind=engine)
session = Session()

Base = sqlalchemy.ext.declarative.declarative_base()

class Loto(Base):
    __tablename__ = 'loto'
    id        = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    times     = sqlalchemy.Column(sqlalchemy.Integer)
    date      = sqlalchemy.Column(sqlalchemy.Date)
    one       = sqlalchemy.Column(sqlalchemy.Integer)
    two       = sqlalchemy.Column(sqlalchemy.Integer)
    three     = sqlalchemy.Column(sqlalchemy.Integer)
    four      = sqlalchemy.Column(sqlalchemy.Integer)
    five      = sqlalchemy.Column(sqlalchemy.Integer)
    six       = sqlalchemy.Column(sqlalchemy.Integer)
    seven     = sqlalchemy.Column(sqlalchemy.Integer)
    bonus_one = sqlalchemy.Column(sqlalchemy.Integer)
    bonus_two = sqlalchemy.Column(sqlalchemy.Integer)

def add_loto(loto):
    loto.to_sql("loto", engine, if_exists = "append", index = False)

def delete_loto():
    s = session.query(Loto)
    s.delete(synchronize_session = 'fetch')
    session.commit()
