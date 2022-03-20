from __future__ import annotations
from typing import List
from pydantic import BaseModel

class Post(BaseModel):
    id: int
    author: str
    authorId: int
    likes: int
    popularity: float
    reads: int
    tags: List[str]

    def __eq__(self, other: Post) -> bool:
        return self.id == other.id and self.authorId == other.authorId
    
    def __hash__(self) -> int:
        return hash(("id", self.id, "author_id", self.authorId))