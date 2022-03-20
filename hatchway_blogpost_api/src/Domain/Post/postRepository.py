import abc
from src.Domain.Post.post import Post
from typing import List

class PostRepository(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def get_tags_saved(self) -> List[str]:
        raise NotImplementedError

    @abc.abstractmethod
    def get_posts_by_tag(self, tag: str) -> List[Post]:
       raise NotImplementedError

    @abc.abstractmethod
    def save_posts(self, tag: str, posts: List[Post]) -> None:
        raise NotImplementedError