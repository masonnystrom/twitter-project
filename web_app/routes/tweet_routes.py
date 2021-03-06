# web_app/routes/tweet_routes.py

from flask import Blueprint, jsonify, render_template, request, redirect
from web_app.models import db, TweetFile, parse_records

tweet_routes = Blueprint("tweet_routes", __name__)

@tweet_routes.route("/tweets.json")
def list_tweets():
    print("REQUESTED THE Tweets IN JSON FORMAT")
    tweet_records = TweetFile.query.all()
    tweets = parse_records(tweet_records)
    return jsonify(tweets)

@tweet_routes.route("/tweets")
def tweets():
    print("VISITED THE TWEETS PAGE")
   
    tweet_records = TweetFile.query.all()
    return render_template("tweets.html", tweets=tweet_records)

@tweet_routes.route("/tweets/new")
def new_tweet():
    return render_template("new_tweet.html")

@tweet_routes.route("/tweets/create", methods=["POST"])
def create_tweet():
    print("FORM DATA:", dict(request.form))
    # store in database
    new_tweet = TweetFile(title=request.form["tweet info"], author_id=request.form["Twitter Account"])
    db.session.add(new_tweet)
    db.session.commit()
    
    return redirect(f"/tweets")
