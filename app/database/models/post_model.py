from sqlalchemy import Column, String,Integer

from app.database.base_class import Base

class PostModel(Base):
    __tablename__= "Blogs"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    body = Column(String)
    date = Column(String)