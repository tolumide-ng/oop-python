from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()


# Create database engine

db_name = 'database.db'
db_path = os.path.join(os.path.dirname(__file__), db_name)
db_uri = os.getenv('database')
engine = create_engine(os.getenv('database'))


# Declarative
Base = declarative_base()
Base.metadata.bind = engine


# Create database session object
db_session = scoped_session(sessionmaker(bind=engine, expire_on_commit=False))
Base.query = db_session.query_property()
