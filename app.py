from flask import Flask, request
import requests

app = Flask(__name__)


@app.route("/")  # this sets the route to this page
def home():
    return "Hello! this is the main page <h1>HELLO</h1>"  # some basic inline htm


@app.route("/movie_page")
def second_page():
    base_api = "https://www.omdbapi.com/"

    title = request.args.get('title')

    search_param = {
        't': title,
        'apikey': '47b63b3a'
    }

    if title:
        response = requests.get(base_api, params=search_param)
        response = response.content.decode('utf-8')
    else:
        response = { 'message': 'Please enter a movie title'}

    return response


if __name__ == "__main__":
    app.run(debug=True)
