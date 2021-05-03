# from lib import user
from flask import Flask, jsonify
import serverless_wsgi

# class CreateUser(TypedDict):
#     username: str
#     email: str
#     interests: List[str]
#     based_in: str

app = Flask(__name__)


@app.route("/")
def add():
    return jsonify(result="test")


@app.route("/create")
def create():
    return jsonify(create="test", feat="test")


@app.route("/remove")
def remove():
    return jsonify(remove="test", feat="test")


def lambda_handler(event, context):
    return serverless_wsgi.handle_request(app, event, context)
