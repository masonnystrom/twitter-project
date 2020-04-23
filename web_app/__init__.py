# web_app/__init__.py
from flask import Flask
import os 
from dotenv import load_dotenv


from web_app.models import db, migrate
from web_app.routes.home_routes import home_routes
from web_app.routes.tweet_routes import tweet_routes
from web_app.routes.twitter_routes import twitter_routes
from web_app.routes.admin_routes import admin_routes
from web_app.routes.stats_routes import stats_routes

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY", default="super secret")

# application factory pattern 
def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = SECRET_KEY # required for flash messaging
    
    # configure the database:
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # suppress warning messages
    
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(home_routes)
    app.register_blueprint(tweet_routes)
    app.register_blueprint(twitter_routes) 
    app.register_blueprint(admin_routes)
    app.register_blueprint(stats_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)