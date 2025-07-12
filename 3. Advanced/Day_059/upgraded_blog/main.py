from flask import Flask, render_template
import requests

app = Flask(__name__)
url = "https://api.npoint.io/22b88247f6a230219a7d"
response = requests.get(url)
posts = response.json()

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for post in posts:
        if post["id"] == index:
            requested_post = post
            post_image = post['image']
    return render_template("post.html", post=requested_post, image=post_image)

if __name__ == "__main__":
    app.run(debug=True)
