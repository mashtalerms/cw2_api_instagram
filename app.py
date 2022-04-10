from flask import Flask, render_template, request, jsonify
from utils import get_posts_all, get_posts_by_user, get_comments_by_post_id, search_for_posts, get_post_by_pk

posts = get_posts_all()

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route("/")
def main():
    return render_template("index.html", posts=posts)


@app.route("/posts/<int:post_id>")
def search_post_by_id(post_id):
    post = get_post_by_pk(post_id)
    comments = get_comments_by_post_id(post_id)
    comments_len = len(comments)
    return render_template("post.html", post=post, comments=comments, comments_len=comments_len)


@app.route("/search/")
def search_by_query():
    all_posts = get_posts_all()
    search_by = request.args.get('s')
    posts_by_query = search_for_posts(search_by)
    return render_template("search.html", all_posts=all_posts, posts_by_query=posts_by_query, posts_by_query_len=len(posts_by_query))


@app.route("/users/<username>")
def user(username):
    posts_by_user = get_posts_by_user(username)
    return render_template("user-feed.html", posts_by_user=posts_by_user)



@app.route("/api/posts", methods=['GET'])
def get_all_posts_in_json():
    data = posts
    return jsonify(data)


@app.route("/api/posts/<int:post_id>", methods=['GET'])
def get_post_in_json(post_id):
    data = get_post_by_pk(post_id)
    return jsonify(data)



if __name__=="__main__":
    app.run(debug=True)


