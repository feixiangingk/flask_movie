#-*-coding:utf-8-*-
# author:       lenovo
# createtime:   2018/4/15 16:36
# software:     PyCharm

from __future__ import unicode_literals
from datetime import datetime
from app.ext import db

class Tag(db.Model):
    '''
    标签
    '''
    __tablename__="tag"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),unique=True)
    add_time=db.Column(db.DateTime,index=True,default=datetime.now)
    movies=db.relationship('Movie',backref='tag')
    def __repr__(self):
        return "<Model Tag {}>".format(self.name)

class Movie(db.Model):
    '''
    电影
    '''
    __tablename__='movie'
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(255),unique=True) #标题
    url=db.Column(db.String(255),unique=True) #地址
    info=db.Column(db.Text) #简介
    logo=db.Column(db.String(255),unique=True) #封面
    star=db.Column(db.SmallInteger) #星级
    playnum=db.Column(db.BigInteger) #播放量
    commentnum=db.Column(db.BigInteger)#评论量
    tag_id=db.Column(db.Integer,db.ForeignKey('tag.id')) #所属标签
    area=db.Column(db.String(255)) #上映地区
    release_time=db.Column(db.Date) #上映时间
    length=db.Column(db.String(100)) #播放时间
    add_time=db.Column(db.DateTime,index=True,default=datetime.now)#添加时间
    comments=db.relationship('Comment',backref='movie') #评论外键关联
    moviecols=db.relationship('Moviecol',backref='movie') #收藏外键关联

    def __repr__(self):
        return "<Model Movie {}>".format(self.title)

class Preview(db.Model):
    """
    上映预告
    """
    __tablename__="preview"
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(255),unique=True) #标题
    logo=db.Column(db.String(255))
    add_time=db.Column(db.DateTime,index=True,default=datetime.now)

    def __repr__(self):
        return "<Model Preview {}>".format(self.title)

class Comment(db.Model):
    __tablename__="comment"
    id=db.Column(db.Integer,primary_key=True)
    content=db.Column(db.Text) #评论内容
    movie_id=db.Column(db.Integer,db.ForeignKey('movie.id')) #所属电影
    user_id=db.Column(db.Integer,db.ForeignKey('user.id')) #所属用户
    add_time=db.Column(db.DateTime,index=True,default=datetime.now)

    def __repr__(self):
        return "<Model Comment {}>".format(self.id)

class Moviecol(db.Model):
    '''
    电影收藏
    '''
    id=db.Column(db.Integer,primary_key=True)
    movie_id=db.Column(db.Integer,db.ForeignKey('movie.id'))
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    add_time = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return "<Model Moviecol {}>".format(self.id)