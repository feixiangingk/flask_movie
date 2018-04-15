#-*-coding:utf-8-*-
# author:       lenovo
# createtime:   2018/4/15 14:15
# software:     PyCharm

def init_views(app):

    @app.route('/')
    def hello_world():
        return 'Hello World!'