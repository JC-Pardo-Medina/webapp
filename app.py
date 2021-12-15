import flask
from flask import Flask,render_template
from werkzeug.wrappers import Request, Response
app = Flask(__name__)

@app.route("/")


def index():
    return render_template("index.html")


if __name__ == "__main__":
    from werkzeug.serving import run_simple
    run_simple('localhost', 9000, app)

