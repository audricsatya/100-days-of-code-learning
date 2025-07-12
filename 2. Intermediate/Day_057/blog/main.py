from flask import Flask, render_template
from post import Post
import requests
import datetime as dt

CURRENT_YEAR = dt.datetime.now().year
posts = requests.get("https://api.npoint.io/308fff4c8c069fd8cd54").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

app = Flask(__name__)

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=post_objects, copy_year=CURRENT_YEAR)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post, copy_year=CURRENT_YEAR)

# if __name__ == "__main__":
#     for post in posts_objects:
#         print(post)
#     app.run(debug=True)


