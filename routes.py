from flask import Blueprint, jsonify

main = Blueprint('main', __name__)

@main.route("/")
def home():
    return jsonify({
        "message": "Flask DevOps Production App Running"
    })