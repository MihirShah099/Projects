from src.Domain.Post.postRepository import PostRepository
from typing import Dict, List
from src.Domain.Post.post import Post

class PostsInMemory(PostRepository):
    def __init__(self) -> None:
        self.posts: Dict[str, List[Post]] = {}

    def get_tags_saved(self) -> List[str]:
        return list(self.posts.keys())

    def get_posts_by_tag(self, tag: str) -> List[Post]:
       return self.posts.get(tag)

    def save_posts(self, tag: str, posts: List[Post]) -> None:
        self.posts[tag] = posts