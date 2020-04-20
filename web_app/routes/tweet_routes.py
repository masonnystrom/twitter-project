# web_app/routes/tweet_routes.py

from flask import Blueprint, jsonify, request, render_template, flash, redirect

tweet_routes = Blueprint("tweet_routes", __name__)

@tweet_routes.route("/tweets.json")
def list_tweets():
    tweets = [
        {"id": 1, "ETH": "ETH is money"},
        {"id": 2, "BTC": "Bitcoin fixes this"},
        {"id": 3, "ZCH": "privacy matters"},
    ]
    return jsonify(tweets)

@tweet_routes.route("/tweets")
def list_tweets_for_humans():
    tweets = [
        {"id": 1, "Ethereum": "ETH is money"},
        {"id": 2, "Bitcoin": "Bitcoin fixes this"},
        {"id": 3, "Zcash": "privacy matters"},
    ]
    return render_template("tweets.html", message="Here's some tweets about crypto", tweets=tweets)

@tweet_routes.route("/tweets/new")
def new_tweet():
    return render_template("new_tweet.html")

@tweet_routes.route("/tweets/create", methods=["POST"])
def create_tweet():
    print("FORM DATA:", dict(request.form))
    # todo: store in database
    return jsonify({
        "message": "Tweet CREATED OK (TODO)",
        "tweet": dict(request.form)
    })
    flash(f"Tweet '{new_tweet.title}' created successfully!", "success")
    return redirect(f"/tweets")
