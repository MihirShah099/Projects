import abc
from .post import Post
from typing import List

class PostApiGateway(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_posts(self, tag: str) -> List[Post]:
        raise NotImplementedError