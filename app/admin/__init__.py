#-*-coding:utf-8-*-
# author:       lenovo
# createtime:   2018/4/15 14:14
# software:     PyCharm
from flask import Blueprint
admin=Blueprint('admin',__name__)
import app.admin.views


