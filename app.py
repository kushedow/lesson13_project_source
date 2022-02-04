from flask import Flask, request, render_template, send_from_directory
from config import POST_PATH, COMMENTS_PATH
import functions


app = Flask(__name__)

posts = functions.get_posts(POST_PATH)
comments = functions.get_comments(COMMENTS_PATH)

@app.route("/")
def index_page():
    return render_template('main_page.html', posts=posts, comments=comments)

@app.route('/search')
def search_by_tag_list():
    tags = functions.get_all_tags(posts)
    return render_template('search.html', tags=tags)

@app.route("/tag", methods=["GET"])
def post_by_tag_page():
    search_tag = request.args.get('search_by_tag')
    posts_match = functions.get_posts_by_tag(search_tag, posts)
    if len(posts_match) > 0:
        return render_template('post_by_tag.html', search_tag=search_tag,
                               posts_match=posts_match, comments=comments)
    return render_template('post_error.html')


@app.route("/new_post", methods=["GET", "POST"])
def page_post_create():
    if request.method == 'GET':
        return render_template('post_form.html')
    if request.method == 'POST':
        if request.files["picture"]:
            if not request.form.get('content'):
                content = ''
            else:
                content = request.form.get('content')
            file = request.files["picture"]
            post = functions.get_new_post(content, file, posts)
            functions.save_post(post)
            return render_template('post_uploaded.html', post=post)

        return f"файла нет"

# так и не понял, зачем мне этот рут
@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)

@app.route("/post/<int:post_id>")
def post_page(post_id):
    post_match = functions.get_posts_by_id(post_id, posts)
    if len(post_match) > 0:
        return render_template('post_page.html', post_match=post_match, comments=comments)
    return render_template('post_error.html')


@app.route("/save_comment", methods=["POST"])
def save_comment():
    comment_text = request.form.get('comment_text')
    post_id = request.form.get('post_id')
    user_name = request.form.get('user_name')
    functions.save_comment(post_id, user_name, comment_text)
    return render_template('comment_uploaded.html')






if __name__ == '__name__':
    app.run(debug=True)


app.run()