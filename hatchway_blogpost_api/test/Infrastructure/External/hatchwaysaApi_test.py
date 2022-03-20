from src.Domain.Post.post import Post
from typing import List
from src.Infrastructure.External.hatchwaysApi import HatchwaysApi
import unittest


class HatchwaysApiTest(unittest.TestCase):

    def test_given_tag_when_calling_external_api_then_api_returns_list_posts(self):
        self.external_api = HatchwaysApi()
        self.SOME_TAGS = "tech"

        posts: List[Post] = self.external_api.get_posts(self.SOME_TAGS)

        self.assertGreater(len(posts), 0)