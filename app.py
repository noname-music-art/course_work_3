from flask import Flask
from main.views import main_blueprint
from post.views import post_blueprint
from search.views import search_blueprint
from user_feed.views import user_feed_blueprint

app = Flask(__name__)


app.register_blueprint(main_blueprint)
app.register_blueprint(post_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(user_feed_blueprint)


app.run()
