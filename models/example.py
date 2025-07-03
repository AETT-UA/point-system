from sqlalchemy import Column, Integer, String, ForeignKey
from utils.DBEngine import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20), nullable=False)
    email = Column(String(50), unique=True, index=True, nullable=False)

    posts = relationship("Post", back_populates="owner")


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(20), nullable=False)
    content = Column(String(100), nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="posts")



