# web_app/routes/home_routes.py

from flask import Blueprint, render_template
from web_app.models import User, Tweet, TweetFile, db 
from web_app.routes.twitter_routes import fetch_user_data

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    # users = User.query.all()
    # user_list = []
    # for user in users:
    #     user_list.append(user.name)
    # print(user_list)
    # return render_template("index.html", userlist=users)

@home_routes.route("/about")
def about():
    return """
    This page is a project to show tweets from crypto Twitter's 
    finest influencers, ethereans, bitcoin maximalists, anarchists, and other
    crypto nom de guerres.
    """