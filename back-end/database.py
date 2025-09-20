from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:12345678@localhost:5432/api_db")
session = sessionmaker(autoflush=False, autocommit=False)
