# web_app/routes/home_routes.py

from flask import Blueprint

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    x = "All your favorite and most hated crytpo tweets"
    return f"Hello Crypto Twitter!{x}"

@home_routes.route("/about")
def about():
    return "This page is a project to show tweets from crypto Twitter."