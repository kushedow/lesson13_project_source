import json

def get_posts(POST_PATH):
    with open(POST_PATH) as file:
        posts = json.load(file)
    return posts

def get_comments(COMMENTS_PATH):
    with open(COMMENTS_PATH) as file:
        comments = json.load(file)
    return comments


def get_posts_by_tag(search_tag, posts):
    posts_match = []
    search_tag = search_tag.lower()
    for post in posts:
        for tag in post['tags']:
            if tag.startswith(search_tag):
                posts_match.append(post)
    return posts_match

def get_posts_by_id(post_id, posts):
    post_match = {}
    for post in posts:
        if post['post_id'] == post_id:
            post_match = post
    return post_match


def new_post_upload():
    pass

