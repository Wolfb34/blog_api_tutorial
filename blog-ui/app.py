import requests
import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    url = os.getenv("PROJECT_API_TEST_SERVICE_PORT")[6:]
    url = "http://" + url
    print(url)
    response = requests.get(url)
    return response.content

if __name__ == "__main__":
    app.run(host="0.0.0.0")
