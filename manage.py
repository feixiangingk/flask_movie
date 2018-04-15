#-*-coding:utf-8-*-
# author:       lenovo
# createtime:   2018/4/15 14:13
# software:     PyCharm
from flask_script import Manager
from app import create_app

app=create_app()
manager=Manager(app)

@manager.command
def dev():
    app.config['DEBUG']=True
    app.run()

if __name__ == '__main__':
    manager.run()


