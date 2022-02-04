import json
from config import POST_PATH, UPLOAD_FOLDER, COMMENTS_PATH

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


def clickable_content(content):
    # вот догадываюсь, что это делается не так, но уже второй час ночи, поэтому костылю, как могу
    words = content.split(' ')
    clickable_content = ""
    clickable_content_list = []
    for word in words:
        if '#' in word:
            word = word.replace('#', '')
            word = f"<a href='/tag?search_by_tag={word}'>" + word +"</a>"
            clickable_content_list.append(word)
        else:
            clickable_content_list.append(word)
    clickable_content = ' '.join(clickable_content_list)
    return clickable_content


def find_tags(content):
    words = content.split(' ')
    tags = []
    for word in words:
        if '#' in word:
            word.replace('#', '')
            tags.append(word)
    return tags

def get_all_tags(posts):
    tags = []
    for post in posts:
        tags = tags + post['tags']
    return tags



def get_new_post(content, file, posts):
    post_id = len(posts) + 1
    tags = find_tags(content)
    filename = file.filename.replace(' ', '-')
    url = f"{UPLOAD_FOLDER}post_id_{str(post_id)}_{filename}"
    file.save(url)
    post = {"post_id": post_id, "content": content,
            "pic": url, "tags": tags}
    return post

def save_post(post):
    with open(POST_PATH) as file:
        posts = json.load(file)
    posts.append(post)

    with open(POST_PATH, 'w') as file:
        json.dump(posts, file, indent=2)