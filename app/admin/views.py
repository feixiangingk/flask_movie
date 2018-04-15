#-*-coding:utf-8-*-
# author:       lenovo
# createtime:   2018/4/15 14:14
# software:     PyCharm

from .import admin
@admin.route("/")
def index():
    return 'hello admin'
