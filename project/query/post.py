from project.post import Post

def get_post(id: str) -> Post:
    return Post(title="Hello, world!")