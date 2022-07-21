from flask import Flask, render_template

from app.main.views import main_blueprint
from app.api.views import api_blueprint
from app import logger

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

logger.create_logger()

app.register_blueprint(main_blueprint)
app.register_blueprint(api_blueprint)


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500


@app.errorhandler(ValueError)
def value_error(error):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run()
