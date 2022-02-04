from flask import Flask, request, render_template, send_from_directory
from config import POST_PATH, UPLOAD_FOLDER, COMMENTS_PATH
import functions


app = Flask(__name__)

posts = functions.get_posts(POST_PATH)
comments = functions.get_comments(COMMENTS_PATH)

@app.route("/")
def index_page():
    return render_template('main_page.html', posts=posts, comments=comments)


@app.route("/tag", methods=["GET"])
def post_by_tag_page():
    search_tag = request.args.get('search_by_tag')
    posts_match = functions.get_posts_by_tag(search_tag, posts)
    if len(posts_match) > 0:
        return render_template('post_by_tag.html', search_tag=search_tag,
                               posts_match=posts_match, comments=comments)
    return render_template('post_error.html')




@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)

@app.route("/post/<int:post_id>")
def post_page(post_id):
    post_match = functions.get_posts_by_id(post_id, posts)
    if len(post_match) > 0:
        return render_template('post_page.html', post_match=post_match, comments=comments)
    return render_template('post_error.html')


if __name__ == '__name__':
    app.run(debug=True)


app.run()