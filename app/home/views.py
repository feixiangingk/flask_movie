#-*-coding:utf-8-*-
# author:       lenovo
# createtime:   2018/4/15 14:15
# software:     PyCharm

from .import home

@home.route('/')
def hello_world():
    return 'Hello World!'