import requests
from typing import Dict, List
from pydantic import parse_obj_as
from src.Domain.Post.post import Post
from src.Domain.Post.postApiGateway import PostApiGateway


class HatchwaysApi(PostApiGateway):
    def get_posts(self, tag: str) -> List[Post]:
        results: Dict[str, List[Post]] = parse_obj_as(Dict[str, List[Post]], requests.get("https://api.hatchways.io/assessment/blog/posts?tag={0}".format(tag)).json())
        return results.get("posts")