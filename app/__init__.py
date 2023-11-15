from flask import Flask
from config import config_by_name


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    # 注册蓝图
    from .views import your_view
    app.register_blueprint(your_view.bp)

    return app
