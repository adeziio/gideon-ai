from flask import Flask, jsonify,  request
from flask_cors import CORS
from dotenv import load_dotenv, find_dotenv
from src import util
from src import model


# Environment Variables
load_dotenv(find_dotenv())

# Flask
app = Flask(__name__)

# Cors
CORS(app)


@app.route("/")
def default():
    return "Gideon is online..."


@app.route("/chat", methods=['POST'])
def quote():
    key = request.headers.get("GIDEON_API_KEY")
    if (util.checkAuth(key)):
        body = request.json
        query = body["query"]
        if (query):
            return jsonify(response=model.run(query))
        return jsonify(error="Invalid parameter")
    return jsonify(error="Unauthorized")


# Main
if __name__ == '__main__':
    app.run()
