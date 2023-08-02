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


@app.route("/gpt-3.5-turbo", methods=['POST'])
def gpt_3_5_turbo():
    key = request.headers.get("GIDEON_API_KEY")
    if (Auth.checkAuth(key)):
        body = request.json
        input = body["input"]
        if (input):
            return jsonify(output=OpenAI.run("gpt-3.5-turbo", input))
        return jsonify(error="Invalid parameter")
    return jsonify(error="Unauthorized")


@app.route("/stable-diffusion", methods=['POST'])
def stable_diffusion():
    key = request.headers.get("GIDEON_API_KEY")
    if (Auth.checkAuth(key)):
        body = request.json
        input = body["input"]
        if (input):
            return jsonify(output=StableDiffusion.run(input))
        return jsonify(error="Invalid parameter")
    return jsonify(error="Unauthorized")


# Main
if __name__ == '__main__':
    app.run()
