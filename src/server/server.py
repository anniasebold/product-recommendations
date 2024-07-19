from flask import Flask
from src.config import Config
from src.routes.product_recommendations_route import product_recommendations_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(product_recommendations_bp)

    return app
