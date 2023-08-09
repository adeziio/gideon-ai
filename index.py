from flask import Flask, jsonify,  request
from flask_cors import CORS
from dotenv import load_dotenv, find_dotenv
from src.utils import Auth
from src.models import OpenAI
from src.models import StableDiffusion


# Environment Variables
load_dotenv(find_dotenv())

# Flask
app = Flask(__name__)

# Cors
CORS(app)


@app.route("/")
def default():
    return "Gideon is online..."


@app.route("/openai", methods=['POST'])
def openai():
    key = request.headers.get("GIDEON_API_KEY")
    if (Auth.checkAuth(key)):
        body = request.json
        input = body["input"]
        model = body["model"]
        if (input and model):
            return jsonify(output=OpenAI.run(model, input))
        return jsonify(error="Invalid parameter")
    return jsonify(error="Unauthorized")


# @app.route("/stable-diffusion", methods=['POST'])
# def stable_diffusion():
#     key = request.headers.get("GIDEON_API_KEY")
#     if (Auth.checkAuth(key)):
#         body = request.json
#         input = body["input"]
#         if (input):
#             return jsonify(output=StableDiffusion.run(input))
#         return jsonify(error="Invalid parameter")
#     return jsonify(error="Unauthorized")


# Main
if __name__ == '__main__':
    app.run()
