from dataclasses import dataclass

from project.post import Post

@dataclass
class AddPostInput:
    title: str

def add_post(input: AddPostInput) -> Post:
    return Post(title=input.title)
