from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
Base = declarative_base()


class products_table(Base):
    __tablename__ = 'products'
    name = Column(String)
    price = Column(Float)
    id = Column(Integer, primary_key=True)
