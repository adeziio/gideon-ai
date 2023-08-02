import os
import openai

from dotenv import load_dotenv, find_dotenv

# Environment Variables
load_dotenv(find_dotenv())

# Initialization
openai.api_key = os.getenv('GIDEON_OPENAI_KEY')


def run(model, input):
    try:
        input = input.lower()
        response = ""
        if ("draw" in input) or ("picture" in input) or ("image" in input) or ("portrait" in input):
            image_resp = openai.Image.create(
                prompt=input,
                n=1,
                size="512x512"
            )
            response = image_resp['data'][0]['url']
        else:
            # create a chat completion
            chat_completion = openai.ChatCompletion.create(
                model=model,
                messages=[{"role": "user", "content": input}]
            )
            response = chat_completion.choices[0].message.content
        return response
    except Exception as e:
        return str(e)
