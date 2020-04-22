# web_app/routes/home_routes.py

from flask import Blueprint, render_template, redirect
from web_app.models import User, Tweet, TweetFile, db 
from web_app.routes.twitter_routes import fetch_user_data

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    return render_template("/make_prediction.html")
