#-*-coding:utf-8-*-
# author:       lenovo
# createtime:   2018/4/15 15:08
# software:     PyCharm
from __future__ import unicode_literals
from datetime import datetime
from app.ext import db

class User(db.Model):
    """
    会员表
    """
    __tablename__="user"
    id=db.Column(db.Integer,primary_key=True) #编号
    name=db.Column(db.String(100),unique=True) #昵称
    pwd=db.Column(db.String(100))
    email=db.Column(db.String(100),unique=True)
    phone=db.Column(db.String(11),unique=True)
    info=db.Column(db.Text) #个性简介
    face=db.Column(db.String(255))
    add_time=db.Column(db.DateTime,index=True,default=datetime.now) #注册时间
    uuid=db.Column(db.String(255),unique=True) #唯一标识符
    userlogs=db.relationship('Userlog',backref='user') #会员日志外键映射
    comments = db.relationship('Comment', backref='user')  # 评论外键关联
    moviecols = db.relationship('Moviecol', backref='user')  # 收藏外键关联

    def __repr__(self):
        return "<Model User {}>".format(self.name)

class Userlog(db.Model):
    __tablename__="userlog"
    id=db.Column(db.Integer,primary_key=True) #编号
    user_id=db.Column(db.Integer,db.ForeignKey('user.id')) #外键关联会员表
    ip=db.Column(db.String(100))
    add_time=db.Column(db.DateTime,index=True,default=datetime.now)

    def __repr__(self):
        return "<Model Userlog {}>".format(self.id)

class Auth(db.Model):
    '''
    权限表
    '''
    __tablename__="auth"
    id=db.Column(db.Integer,primary_key=True) #编号
    name=db.Column(db.String(100),unique=True) #昵称
    url=db.Column(db.String(255),unique=True)
    add_time=db.Column(db.DateTime,index=True,default=datetime.now)
    def __repr__(self):
        return "<Model Auth {}>".format(self.name)

class Role(db.Model):
    __tablename__='role'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),unique=True) #名称
    auths=db.Column(db.String(600))
    add_time = db.Column(db.DateTime, index=True, default=datetime.now)
    admins=db.relationship('Admin',backref='role')
    def __repr__(self):
        return "<Model Role {}>".format(self.name)

    @staticmethod
    def insert_init_role():
        role = Role(name="超级管理员", auths="")
        db.session.add(role)
        db.session.commit()

class Admin(db.Model):
    '''
    管理员表
    '''
    __tablename__='admin'
    id=db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100), unique=True)  # 昵称
    pwd = db.Column(db.String(100))
    is_super=db.Column(db.SmallInteger) #是否为超级管理员
    role_id=db.Column(db.Integer,db.ForeignKey('role.id'))  #所属角色
    add_time = db.Column(db.DateTime, index=True, default=datetime.now)
    adminlogs = db.relationship('Adminlog', backref='admin')
    oplogs = db.relationship('Oplog', backref='admin')

    def __repr__(self):
        return "<Model Admin {}>".format(self.name)

    @staticmethod
    def insert_init_admin():
        from werkzeug.security import generate_password_hash
        admin = Admin(name='admin', pwd=generate_password_hash('admin'),
                      is_super=0, role_id=1)
        db.session.add(admin)
        db.session.commit()

class Adminlog(db.Model):
    '''
    管理员日志表
    '''
    __tablename__="adminlog"
    id=db.Column(db.Integer,primary_key=True) #编号
    admin_id=db.Column(db.Integer,db.ForeignKey('admin.id')) #外键关联管理员表
    ip=db.Column(db.String(100))
    add_time=db.Column(db.DateTime,index=True,default=datetime.now)

    def __repr__(self):
        return "<Model Adminlog {}>".format(self.id)

class Oplog(db.Model):
    '''
    操作日志志表
    '''
    __tablename__="oplog"
    id=db.Column(db.Integer,primary_key=True) #编号
    admin_id=db.Column(db.Integer,db.ForeignKey('admin.id')) #外键关联管理员表
    ip=db.Column(db.String(100)) #登录ip
    reason=db.Column(db.String(600)) #操作细节
    add_time=db.Column(db.DateTime,index=True,default=datetime.now)

    def __repr__(self):
        return "<Model Oplog {}>".format(self.id)



