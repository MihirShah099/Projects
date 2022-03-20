from __future__ import annotations
from src.Domain.Post.post import Post
from typing import List

class PostBuilder:
    def __init__(self) -> None:
        self.id: int = 1
        self.author: str = "Some author"
        self.authorId: int = 10
        self.likes: int = 150
        self.popularity: float = 0.95
        self.reads: int = 10
        self.tags: List[str] = ["tech"]

    def set_id(self, id: int) -> PostBuilder:
        self.id = id
        return self

    def set_author(self, author: str) -> PostBuilder:
        self.author = author
        return self

    def set_author_id(self, author_id: int) -> PostBuilder:
        self.authorId = author_id
        return self

    def set_likes(self, likes: int) -> PostBuilder:
        self.likes = likes
        return self

    def set_popularity(self, popularity: float) -> PostBuilder:
        self.popularity = popularity
        return self

    def set_reads(self, reads: int) -> PostBuilder:
        self.reads = reads
        return self

    def set_tags(self, tags: List[str]) -> PostBuilder:
        self.tags = tags
        return self

    def add_tag(self, tag: str) -> PostBuilder:
        self.tags.append(tag)
        return self

    def buildPost(self) -> Post:
        return Post(**{
            "id": self.id,
            "author": self.author,
            "authorId": self.authorId,
            "likes": self.likes,
            "popularity": self.popularity,
            "reads": self.reads,
            "tags": self.tags
        })
