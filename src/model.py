import os
import openai

from dotenv import load_dotenv, find_dotenv
from src import util


# Environment Variables
load_dotenv(find_dotenv())

# Initialization
openai.api_key = os.getenv('GIDEON_OPENAI_KEY')


def run(query):
    try:
        response = ""
        if ("draw" in query) or ("picture" in query) or ("image" in query):
            image_resp = openai.Image.create(
                prompt=query,
                n=1,
                # size="512x512"
            )
            response = image_resp
        else:
            # create a chat completion
            chat_completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": query}]
            )
            response = chat_completion.choices[0].message.content
        return response
    except Exception as e:
        return str(e)
