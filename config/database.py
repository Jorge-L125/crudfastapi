from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

usernamedb = 'postgres'
passworddb = 'jorge123'
hostdb = 'localhost'
port = 5432
database = 'postgres'

database_url = f"postgresql://{usernamedb}:{passworddb}@{hostdb}:{port}/{database}"
engine = create_engine(database_url)
Session = sessionmaker(engine)
session = Session()
Base = declarative_base()
  