'''
DB Helper
'''

__author__ = 'Sabbir'
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from appcore.helpers.configs import DB_CONFIG

ENGINE = create_engine(DB_CONFIG, convert_unicode=True, echo=True)


DB_SESSION = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=ENGINE))

BASE = declarative_base()
BASE.query = DB_SESSION.query_property()


def init_db():
    '''
    Execute database
    '''
    BASE.metadata.create_all(bind=ENGINE)
