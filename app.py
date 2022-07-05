from flask import Flask, render_template
from main.views import main_blueprint
from post.views import post_blueprint
from search.views import search_blueprint
from user_feed.views import user_feed_blueprint

app = Flask(__name__)


app.register_blueprint(main_blueprint)
app.register_blueprint(post_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(user_feed_blueprint)


@app.errorhandler(404)
def page_not_found_error(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500


app.run()
