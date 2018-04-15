from flask import Flask
from admin import admin as admin_blueprint
from home import home as home_blueprint
from app.config import DEVConfig
from ext import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(DEVConfig)
    app.register_blueprint(admin_blueprint,url_prefix="/admin")
    app.register_blueprint(home_blueprint)
    db.init_app(app)
    return app



if __name__ == '__main__':
    app=create_app()
    app.run(debug=True)
