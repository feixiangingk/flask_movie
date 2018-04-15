from flask import Flask
from home.views import init_views


def create_app():
    app = Flask(__name__)
    init_views(app)
    return app



if __name__ == '__main__':
    app=create_app()
    app.run(debug=True)
