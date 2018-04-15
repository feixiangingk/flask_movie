#-*-coding:utf-8-*-
# author:       lenovo
# createtime:   2018/4/15 15:08
# software:     PyCharm
import pymysql

class DEVConfig(object):
    DEBUG=True
    DATABASE_USER = 'root'
    DATABASE_PWD = "123456"
    DATABASE_HOST = '127.0.0.1'
    DATABASE_PORT = 3306
    DATABASE_NAME = 'flask_movie'
    SQLALCHEMY_DATABASE_URI = 'mysql://' + DATABASE_USER + ':' + DATABASE_PWD + '@' + \
                              DATABASE_HOST + ':' + str(DATABASE_PORT) + '/' + DATABASE_NAME + '?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
