from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/About")
def about():
    x = 2 + 2
    return f"About Me {x}"