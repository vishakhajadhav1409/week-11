from flask import Flask
from app.routes import main
from app.health import health
import logging

def create_app():
    app = Flask(__name__)

    app.config.from_object("app.config.Config")

    app.register_blueprint(main)
    app.register_blueprint(health)

    logging.basicConfig(
        filename='logs/app.log',
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(message)s'
    )

    return app