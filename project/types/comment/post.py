from project.post import Post
from project.comment import Comment

def get_post(root: Comment) -> Post:
    return Post(title="Hello, world!")