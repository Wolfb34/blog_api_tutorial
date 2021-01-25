import requests
import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    url = os.getenv("PROJECT_API_TEST_SERVICE_PORT")[6:]
    url = "http://" + url + "/api/v1/blogposts"
    print(url)
    response = requests.get(url)
    blog_string = response.content
    blog_temp = blog_string.strip('][')
    print(blog_temp)
    if not blog_temp:
        return render_template("empty.html")
    blog_list = blog_temp.split(", ")
    return render_template("index.html", members=blog_list)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
