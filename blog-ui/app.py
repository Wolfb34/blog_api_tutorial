import requests
import os
from flask import Flask, render_template

app = Flask(__name__)
base_url = "http://" + os.getenv(os.getenv("API_ENV_NAME"))[6:]

@app.route('/')
def index():
    url = base_url + "/api/v1/blogposts"
    print(url)
    response = requests.get(url)
    blog_json = response.json()
    print(blog_json)
    if not blog_json:
        return render_template("empty.html")
    return render_template("index.html", members=blog_json)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
