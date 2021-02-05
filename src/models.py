import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_to_id = Column(Integer, ForeignKey('user.id'))
    user_from_id = relationship('User', back_populates="follower")

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    fname = Column(String(50), nullable=False)
    lname = Column(String(50), nullable=False)
    email = Column(String(250), nullable=False)
    posts = relationship("Post", back_populates="user")
    followers= relationship("Follower", back_populates="user")

    def to_dict(self):
        return {}

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    media_type = Column(Enum('Image' 'Video'), nullable=False, server_default='Image')
    url = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))

class Post(Base):
    __tablename__ = 'post'
    id = Column (Integer, primary_key=True)
    post_text = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey ('user.id'))
    media = relationship("Media", back_populates="post")
    comments = relationship("Comment", back_populates="post")

    def to_dict(self):
        return {}

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column (String(250), nullable=False)
    author = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

    def to_dict(self):
        return {}


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')