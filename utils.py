import json

posts = []


def get_posts_all():
    """
    возвращает посты
    """
    global posts
    with open("data/data.json", encoding="UTF-8") as fp:
        posts = json.load(fp)
        return posts


def get_posts_by_user(user_name):
    """
    возвращает посты определенного пользователя
    """
    names = []
    for post in posts:
        names.append(post['poster_name'])
    if user_name not in names:
        raise ValueError("Этого имени нет")
    posts_by_name = []
    for post in posts:
        if user_name == post["poster_name"]:
            posts_by_name.append(post)
    return posts_by_name


def get_comments_by_post_id(post_id):
    """
    возвращает комментарии определенного поста
    """
    if type(post_id) not in [int]:
        raise TypeError("Должно быть int")
    if post_id < 0:
        raise ValueError("Должно быть больше 0")
    with open("data/comments.json", encoding="UTF-8") as fp_1:
        comments = json.load(fp_1)
        comments_by_post = []
        for comment in comments:
            if post_id == comment["post_id"]:
                comments_by_post.append(comment)
        return comments_by_post


def search_for_posts(query):
    """
    возвращает список постов по ключевому слову
    """
    posts_with_query = [x for x in posts if query.lower() in x["content"].lower()]
    return posts_with_query


def get_post_by_pk(pk):
    """
    возвращает один пост по его идентификатору
    """
    if type(pk) not in [int]:
        raise TypeError("Должно быть int")
    if pk <= 0:
        raise ValueError("Должно быть больше 0")
    if pk > len(posts):
        raise ValueError(f"Должно быть меньше {len(posts) + 1}")
    for post in posts:
        if pk == post["pk"]:
            return post


def get_keys_from_json():
    keys = posts[0].keys()
    return keys
