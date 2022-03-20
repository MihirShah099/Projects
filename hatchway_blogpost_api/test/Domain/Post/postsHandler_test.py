from src.Domain.Post.directionsValues import DirectionsValues
from src.Domain.Post.sortByValues import SortByValues
from src.Domain.Post.postsHandler import PostHandler
from test.util.postBuilder import PostBuilder
from typing import List
import unittest

from src.Domain.Post.post import Post

class postHandlerTest(unittest.TestCase):
    
    def setUp(self) -> None:
        SOME_POST_TECH: Post = self._create_post(
            1,
            "Alpha",
            10,
            0.86,
            100,
            1000,
            ["tech", "software", "jobs"]
        )
        SOME_POST_FOOD: Post = self._create_post(
            2,
            "Bravo",
            20,
            0.99,
            150,
            2000,
            ["food", "kitchen", "restaurant"]
        )
        SOME_POST_TRAVEL: Post = self._create_post(
            3,
            "Charlie",
            30,
            0.11,
            300,
            3000,
            ["travel", "culture", "tourist"]
        )
        SOME_POST_GARDEN: Post = self._create_post(
            2,
            "Bravo",
            10,
            0.86,
            100,
            3001,
            ["garden", "vegtables", "herbs", "water", "soil"]
        )
        self.SOME_POSTS: List[Post] = [SOME_POST_TECH, SOME_POST_FOOD, SOME_POST_TRAVEL, SOME_POST_GARDEN]


    def test_when_sorting_posts_ascending_by_id_then_posts_are_sorted_by_id_and_ascending(self):
        sort_posts_by_ascending_id: List[Post] = PostHandler().sort_posts(self.SOME_POSTS, SortByValues.id, DirectionsValues.asc)
        expected_sort_posts: List[Post] = self._sort_posts(self.SOME_POSTS, SortByValues.id, False)

        self.assertListEqual(expected_sort_posts, sort_posts_by_ascending_id)

    def test_when_sorting_posts_descending_by_id_then_posts_are_sorted_by_id_and_descending(self):
        sort_posts_by_asc_id: List[Post] = PostHandler().sort_posts(self.SOME_POSTS, SortByValues.id, DirectionsValues.desc)
        expected_sort_posts: List[Post] = self._sort_posts(self.SOME_POSTS, SortByValues.id, True)

        self.assertListEqual(expected_sort_posts, sort_posts_by_asc_id)

    def test_given_sort_by_id_value_only_when_sorting_posts_then_posts_are_sorted_by_id_and_ascending_by_default(self):
        sort_by_id: str = SortByValues.id
        direction: str = None
        
        sort_posts_by_id: List[Post] = PostHandler().sort_posts(self.SOME_POSTS, sort_by_id, direction)
        expected_sort_posts: List[Post] = self._sort_posts(self.SOME_POSTS, SortByValues.id, False)

        self.assertListEqual(expected_sort_posts, sort_posts_by_id)

    def test_given_direction_ascending_only_when_sorting_posts_then_posts_are_sorted_by_id_default_and_ascending(self):
        sort_by: str = None
        direction: str = DirectionsValues.asc
        
        sort_posts_by_id: List[Post] = PostHandler().sort_posts(self.SOME_POSTS, sort_by, direction)
        expected_sort_posts: List[Post] = self._sort_posts(self.SOME_POSTS, SortByValues.id, False)

        self.assertListEqual(expected_sort_posts, sort_posts_by_id)
    
    def test_given_direction_descending_only_when_sorting_posts_then_posts_are_sorted_by_id_default_and_descending(self):
        direction: str = DirectionsValues.desc
        sort_by: str = None

        sort_posts_by_id: List[Post] = PostHandler().sort_posts(self.SOME_POSTS, sort_by, direction)
        
        expected_sort_posts: List[Post] = self._sort_posts(self.SOME_POSTS, SortByValues.id, True)
        self.assertListEqual(expected_sort_posts, sort_posts_by_id)
    
    def test_given_no_direction_and_no_sort_by_value_when_sorting_posts_then_posts_are_sorted_by_id_and_ascending_default(self):
        sort_by: str = None
        direction: str = None

        sort_posts: List[Post] = PostHandler().sort_posts(self.SOME_POSTS, sort_by, direction)
        expected_sort_posts: List[Post] = self._sort_posts(self.SOME_POSTS, SortByValues.id, False)
        
        self.assertListEqual(expected_sort_posts, sort_posts)


    def test_when_sorting_posts_ascending_by_reads_then_posts_are_sorted_by_reads_and_ascending(self):
        sort_posts_by_asc_read: List[Post] = PostHandler().sort_posts(self.SOME_POSTS, SortByValues.reads, DirectionsValues.asc)
        expected_sort_posts: List[Post] = self._sort_posts(self.SOME_POSTS, SortByValues.reads, False)

        self.assertListEqual(expected_sort_posts, sort_posts_by_asc_read)
    
    def test_when_sorting_posts_descending_by_reads_then_posts_are_sorted_by_reads_and_descending(self):
        sort_posts_by_asc_reads: List[Post] = PostHandler().sort_posts(self.SOME_POSTS, SortByValues.reads, DirectionsValues.desc)
        expected_sort_posts: List[Post] = self._sort_posts(self.SOME_POSTS, SortByValues.reads, True)

        self.assertListEqual(expected_sort_posts, sort_posts_by_asc_reads)
    
    def test_given_sort_by_reads_value_only_when_sorting_posts_then_posts_are_sorted_by_reads_and_ascending_default(self):
        sort_by: str = SortByValues.reads
        direction: str = None

        sort_posts: List[Post] = PostHandler().sort_posts(self.SOME_POSTS, sort_by, direction)
        expecpted_sort_posts: List[Post] = self._sort_posts(self.SOME_POSTS, SortByValues.reads, False)
        
        self.assertListEqual(expecpted_sort_posts, sort_posts)


    def test_when_sorting_posts_ascending_by_likes_then_posts_are_sorted_by_likes_and_ascending(self):
        sort_posts_by_asc_id: List[Post] = PostHandler().sort_posts(self.SOME_POSTS, SortByValues.likes, DirectionsValues.asc)
        expected_sort_posts: List[Post] = self._sort_posts(self.SOME_POSTS, SortByValues.likes, False)

        self.assertListEqual(expected_sort_posts, sort_posts_by_asc_id)
    
    def test_when_sorting_posts_descending_by_likes_then_posts_are_sorted_by_likes_and_descending(self):
        sort_posts_by_asc_id: List[Post] = PostHandler().sort_posts(self.SOME_POSTS, SortByValues.likes, DirectionsValues.desc)
        expected_sort_posts: List[Post] = self._sort_posts(self.SOME_POSTS, SortByValues.likes, True)

        self.assertListEqual(expected_sort_posts, sort_posts_by_asc_id)
    
    def test_given_sort_by_likes_value_only_when_sorting_posts_then_posts_are_sorted_by_likes_and_ascending_default(self):
        sort_by: str = SortByValues.likes
        direction: str = None

        sort_posts: List[Post] = PostHandler().sort_posts(self.SOME_POSTS, sort_by, direction)
        expecpted_sort_posts: List[Post] = self._sort_posts(self.SOME_POSTS, SortByValues.likes, False)

        self.assertListEqual(expecpted_sort_posts, sort_posts)


    def test_when_sorting_posts_ascending_by_popularity_then_posts_are_sorted_by_popularity_and_ascending(self):
        sort_posts_by_asc_id: List[Post] = PostHandler().sort_posts(self.SOME_POSTS, SortByValues.popularity, DirectionsValues.asc)
        expected_sort_posts: List[Post] = self._sort_posts(self.SOME_POSTS, SortByValues.popularity, False)

        self.assertListEqual(expected_sort_posts, sort_posts_by_asc_id)
    
    def test_when_sorting_posts_descending_by_popularity_then_posts_are_sorted_by_popularity_and_descending(self):
        sort_posts_by_asc_id: List[Post] = PostHandler().sort_posts(self.SOME_POSTS, SortByValues.popularity, DirectionsValues.desc)
        expected_sort_posts: List[Post] = self._sort_posts(self.SOME_POSTS, SortByValues.popularity, True)

        self.assertListEqual(expected_sort_posts, sort_posts_by_asc_id)

    def test_given_sort_by_popularity_value_only_when_sorting_posts_then_posts_are_sorted_by_likes_and_ascending_default(self):
        sort_by: str = SortByValues.popularity
        direction: str = None

        sort_posts: List[Post] = PostHandler().sort_posts(self.SOME_POSTS, sort_by, direction)
        expecpted_sort_posts: List[Post] = self._sort_posts(self.SOME_POSTS, SortByValues.popularity, False)

        self.assertListEqual(expecpted_sort_posts, sort_posts)
    
    def test_given_list_with_duplicate_posts_when_removing_duplicate_posts_then_all_duplicates_are_removed(self):
        duplicates_posts: List[Post] = self.SOME_POSTS.copy()
        duplicates_posts.extend([self.SOME_POSTS[0], self.SOME_POSTS[2]])

        unique_list_posts: List[Post] = PostHandler().remove_duplicate_posts(duplicates_posts)
        unique_list_posts = PostHandler().sort_posts(unique_list_posts, SortByValues.id, DirectionsValues.asc)

        self.SOME_POSTS = PostHandler().sort_posts(self.SOME_POSTS, SortByValues.id, DirectionsValues.asc)

        self.assertCountEqual(self.SOME_POSTS, unique_list_posts)
        self.assertTrue(self._compare_if_two_list_posts_are_samed(self.SOME_POSTS, unique_list_posts))

    def _create_post(self, id: int, author: str, author_id: int, likes: int, popularity: float, reads: int, tags: List[str]) -> Post:
        return PostBuilder().set_id(id).set_author(author).set_author_id(author_id).set_likes(likes).set_popularity(popularity).set_reads(reads).set_tags(tags).buildPost()

    def _sort_posts(self, posts: List[Post], sorting_attribute: str, is_reversed: bool) -> List[Post]:
        return sorted(posts, key=lambda post: post.dict().get(sorting_attribute), reverse=is_reversed)
    
    def _compare_if_two_list_posts_are_samed(self, posts_reference: List[Post], posts_to_compare: List[Post]) -> bool:
        return len(set(posts_reference).difference(posts_to_compare)) == 0
