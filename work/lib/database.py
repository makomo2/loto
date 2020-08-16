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
    id       = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    kind     = sqlalchemy.Column(sqlalchemy.String)
    times    = sqlalchemy.Column(sqlalchemy.Integer)
    date     = sqlalchemy.Column(sqlalchemy.Date)
    numbers  = sqlalchemy.Column(sqlalchemy.String)
    bonus    = sqlalchemy.Column(sqlalchemy.String)

def add_loto(loto):
    loto.to_sql("loto", engine, if_exists = "append", index = False)

def delete_loto(kind, min_times, max_times):
    s = session.query(Loto).filter(Loto.kind == kind, Loto.times >= min_times, Loto.times <= max_times)
    s.delete(synchronize_session = 'fetch')
    session.commit()
