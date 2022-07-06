import logging.config

from flask import Flask, render_template

from api.views import api_blueprint
from main.views import main_blueprint
from post.views import post_blueprint
from search.views import search_blueprint
from user_feed.views import user_feed_blueprint

logging.config.fileConfig('logging.ini', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

app = Flask(__name__)


app.register_blueprint(main_blueprint)
app.register_blueprint(post_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(user_feed_blueprint)
app.register_blueprint(api_blueprint)


@app.errorhandler(404)
def page_not_found_error(e):
    logger.error('404')
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    logger.error('500')
    return render_template("500.html"), 500


app.run()
