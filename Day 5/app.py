from flask import Flask, jsonify

app = Flask(__name__)

from routes.product import bp

app.register_blueprint(bp)

@app.route("/")
def home():
    return "<p>Hello, World!</p>"

@app.route('/testing')
def testing():
    return jsonify({"message": "Hello, World!"})