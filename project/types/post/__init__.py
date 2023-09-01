from dataclasses import dataclass

from project.comment import Comment

@dataclass
class Post:
    title: str
    comments: list[Comment] = []