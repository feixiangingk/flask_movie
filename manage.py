#-*-coding:utf-8-*-
# author:       lenovo
# createtime:   2018/4/15 14:13
# software:     PyCharm
from __future__ import unicode_literals
from flask_script import Manager
from app import create_app
from app.ext import db
from flask_migrate import Migrate,MigrateCommand
from app.admin.models import User,Userlog,Role,Admin
from app.home.models import Movie,Tag,Preview,Comment

migrate=Migrate()
app=create_app()
manager=Manager(app)
migrate.init_app(app,db)

manager.add_command("db",MigrateCommand)


@manager.shell
def make_shell_context():
    '''
    创建一个载入预设配置的上下文环境，不用在Python console一步步导包了
    后期还可以将db 等传进来
    :return:
    '''
    return dict(app=app,db=db,User=User,Movie=Movie,
                Preview=Preview,Tag=Tag,Comment=Comment)

@manager.command
def db_data_init():
    """
    添加初始化数据命令;
    注意，此命令需要在创建库成功以后。所以先要执行下列操作：
    python manage.py db init
    python manage.py db migrate -m "create tables"
    python manage.py db upgrade
    :return:
    """
    Role.insert_init_role()
    Admin.insert_init_admin()



@manager.command
def dev():
    app.config['DEBUG']=True
    app.run()



if __name__ == '__main__':
    manager.run()


