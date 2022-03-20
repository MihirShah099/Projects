from typing import List
from test.util.postBuilder import PostBuilder
from src.Domain.Post.post import Post
import unittest
from src.Domain.Post.postRepository import PostRepository
from src.Infrastructure.Persistence.PostsInMemory import PostsInMemory

class PostInMemoryTest(unittest.TestCase):

    def setUp(self) -> None:
        self.SOME_TECH_TAG_KEY: str = "tech"
        self._ALPHA_POST: Post = PostBuilder().set_id(2).set_author_id(20).add_tag("science").buildPost()
        self._BRAVO_POST: Post = PostBuilder().add_tag("music").buildPost()
        self.postRepository: PostRepository = PostsInMemory()
        self.posts_saved: List[Post] = []
        self.posts_saved.append(self._ALPHA_POST)
        self.posts_saved.append(self._BRAVO_POST)
        
    def test_given_posts_is_saved_when_find_by_tag_then_posts_is_retrived(self):
        self.postRepository.save_posts(self.SOME_TECH_TAG_KEY, self.posts_saved)

        retrived_posts: List[Post]  = self.postRepository.get_posts_by_tag(self.SOME_TECH_TAG_KEY)

        self.assertCountEqual(retrived_posts, self.posts_saved)
        self.assertListEqual(retrived_posts, self.posts_saved)

    def test_given_multiple_posts_is_saved_when_find_by_tag_then_only_posts_with_specified_tag_is_retrived(self):
        SOME_POST: Post = PostBuilder().set_id(3).set_author_id(30).set_author("Alphonse").set_tags(["travel", "food"]).buildPost()
        SOME_TAG_KEY: str = "travel"
        self.postRepository.save_posts(SOME_TAG_KEY, [SOME_POST])
        self.postRepository.save_posts(self.SOME_TECH_TAG_KEY, self.posts_saved)

        retrived_posts_with_tech_tag: List[Post] = self.postRepository.get_posts_by_tag(self.SOME_TECH_TAG_KEY)

        self.assertCountEqual(retrived_posts_with_tech_tag, self.posts_saved)
        self.assertListEqual(retrived_posts_with_tech_tag, self.posts_saved)

    def test_given_multiple_posts_is_saved_when_get_tags_saved_then_all_tags_registered_is_retrived(self):
        SOME_TRAVEL_POST: Post = PostBuilder().set_id(3).set_author_id(30).set_tags(["travel", "food"]).buildPost()
        SOME_FOOD_TAG_KEY: str = "food"
        EXPECTED_TAG_KEYS: List[str] = [SOME_FOOD_TAG_KEY, self.SOME_TECH_TAG_KEY]
        self.postRepository.save_posts(SOME_FOOD_TAG_KEY, [SOME_TRAVEL_POST])
        self.postRepository.save_posts(self.SOME_TECH_TAG_KEY, self.posts_saved)
    

        tags_registered: List[str] = self.postRepository.get_tags_saved()

        self.assertCountEqual(EXPECTED_TAG_KEYS, tags_registered)
        self.assertListEqual(sorted(EXPECTED_TAG_KEYS), sorted(tags_registered))
