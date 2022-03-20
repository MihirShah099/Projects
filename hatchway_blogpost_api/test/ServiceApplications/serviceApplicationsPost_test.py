
from test.util.postBuilder import PostBuilder
from typing import Dict, List, Optional
import unittest
from unittest.mock import Mock, patch

from src.Domain.Post.post import Post
from src.Domain.Post.postApiGateway import PostApiGateway
from src.Domain.Post.postRepository import PostRepository
from src.Domain.Post.postsHandler import PostHandler
from src.Domain.Tag.tagHandler import TagHandler
from src.Domain.Post.sortByValues import SortByValues
from src.Domain.Post.directionsValues import DirectionsValues
from src.ServiceApplications.ServiceApplicationsPost import ServiceApplicationPost


class ServiceApplicationPostTest(unittest.TestCase):
    
    def setUp(self) -> None:
        self.SOME_TECH_TAG: str = "tech"
        self.SOME_CRYPTO_TAG: str = "crypto"
        self.SOME_TRAVEL_TAG: str = "travel"
        self.SAMPLE_POSTS_BY_TAG: Dict[str, List[Post]] = self._create_sample_posts_by_tags()


    def test_when_getting_posts_then_all_tags_saved_is_retrived(self):
        some_tags_saved: List[str] = [self.SOME_TECH_TAG, self.SOME_CRYPTO_TAG]
        some_tags_input: str = ",".join(some_tags_saved)
        self._create_mocks_and_dependecies(some_tags_saved, [], [], None, None)

        self.service_application_post.get_posts(some_tags_input, SortByValues.id, DirectionsValues.asc)

        self.post_repository.get_tags_saved.assert_called_once()

    def test_when_getting_posts_then_sort_posts_and_remove_duplicate_posts_are_called(self):
        some_tags_saved: List[str] = [self.SOME_TECH_TAG, self.SOME_TRAVEL_TAG]
        some_tags_input: str = ",".join(some_tags_saved)
        some_posts_from_tags: List[Post] = self._get_posts_by_tag(some_tags_input)
        self._create_mocks_and_dependecies(some_tags_saved, some_posts_from_tags, [], some_tags_input, None)

        self.service_application_post.get_posts(some_tags_input, SortByValues.id, DirectionsValues.asc)

        self.post_handler.remove_duplicate_posts.assert_called_once_with(some_posts_from_tags)
        self.post_handler.sort_posts.assert_called_once_with(some_posts_from_tags, SortByValues.id, DirectionsValues.asc)
    
    def test_when_getting_posts_then_filter_new_tags_and_common_new_are_called(self):
        some_tags_saved: List[str] = [self.SOME_CRYPTO_TAG]
        some_tags_input: str = ",".join(some_tags_saved)
        some_posts_from_tags: List[Post] = self._get_posts_by_tag(some_tags_input)
        self._create_mocks_and_dependecies(some_tags_saved, some_posts_from_tags, [], some_tags_input, None)
       
        self.service_application_post.get_posts(some_tags_input, None, None)

        self.tag_handler.filter_new_tags.assert_called_once_with(some_tags_input, some_tags_saved)
        self.tag_handler.filter_common_tags.assert_called_once_with(some_tags_input, some_tags_saved)
    
    def test_given_empty_posts_from_repository_when_getting_posts_then_posts_are_retrived_from_external_api_only_and_saved_in_repository(self):
        some_tags_saved: List[str] = []
        some_tags_input: str = "{0},{1}".format(self.SOME_CRYPTO_TAG, self.SOME_TECH_TAG)
        some_posts_from_repository: List[Post] = []
        some_posts_from_external_api: List[Post] = self._get_posts_by_tag(some_tags_input)
        self._create_mocks_and_dependecies(some_tags_saved, some_posts_from_repository, some_posts_from_external_api, None, some_tags_input)

        self.service_application_post.get_posts(some_tags_input, SortByValues.id, DirectionsValues.asc)

        self.post_repository.get_posts_by_tag.assert_not_called()
        self.assertEqual(len(some_tags_input.split(",")), self.post_repository.save_posts.call_count)
        self.assertEqual(len(some_tags_input.split(",")), self.post_api_gateway.get_posts.call_count)

    def test_given_string_with_new_tags_when_getting_posts_then_posts_are_retrived_from_api_only_and_saved_in_repository(self):
        some_tags_saved: List[str] = [self.SOME_TRAVEL_TAG]
        some_tags_input: str = "{0},{1}".format(self.SOME_CRYPTO_TAG, self.SOME_TECH_TAG)
        some_posts_from_repository: List[Post] = self._get_posts_by_tag(self.SOME_TECH_TAG)
        some_posts_from_external_api: List[Post] = self._get_posts_by_tag(some_tags_input)
        self._create_mocks_and_dependecies(some_tags_saved, some_posts_from_repository, some_posts_from_external_api, None, some_tags_input)

        self.service_application_post.get_posts(some_tags_input, SortByValues.id, DirectionsValues.asc)

        self.post_repository.get_posts_by_tag.assert_not_called()
        self.assertEqual(len(some_tags_input.split(",")), self.post_repository.save_posts.call_count)
        self.assertEqual(len(some_tags_input.split(",")), self.post_api_gateway.get_posts.call_count)


    def test_given_string_with_common_tags_when_getting_posts_then_posts_are_retrived_from_post_repository_only(self):
        some_tags_saved: List[str] = [self.SOME_TRAVEL_TAG, self.SOME_TECH_TAG]
        some_tags_input: str = ",".join(some_tags_saved)
        some_posts_from_repository: List[Post] = self._get_posts_by_tag(some_tags_input)
        some_posts_from_external_api: List[Post] = []
        self._create_mocks_and_dependecies(some_tags_saved, some_posts_from_repository, some_posts_from_external_api, some_tags_input, None)

        self.service_application_post.get_posts(some_tags_input, SortByValues.id, DirectionsValues.asc)

        self.post_api_gateway.get_posts.assert_not_called()
        self.post_repository.save_posts.assert_not_called()
        self.assertEqual(len(some_tags_input.split(",")), self.post_repository.get_posts_by_tag.call_count)

    def test_given_string_with_new_and_common_tags_when_getting_posts_then_posts_are_retrived_from_post_repository_and_from_external_api(self):
        some_tags_saved: List[str] = [self.SOME_TECH_TAG, self.SOME_CRYPTO_TAG]
        some_common_tags: str = ",".join(some_tags_saved)
        some_new_tags: str = self.SOME_TRAVEL_TAG
        some_posts_from_repository: List[Post] = self._get_posts_by_tag(some_common_tags)
        some_posts_from_external_api: List[Post] = self._get_posts_by_tag(some_new_tags)
        some_tags_input: str = some_common_tags + "," + some_new_tags
        self._create_mocks_and_dependecies(some_tags_saved, some_posts_from_repository, some_posts_from_external_api, some_common_tags, some_new_tags)

        self.service_application_post.get_posts(some_tags_input, SortByValues.id, DirectionsValues.asc)

        self.assertEqual(len(some_common_tags.split(",")), self.post_repository.get_posts_by_tag.call_count)
        self.assertEqual(len(some_new_tags.split(",")), self.post_api_gateway.get_posts.call_count)
        self.assertEqual(len(some_new_tags.split(",")), self.post_repository.save_posts.call_count)

    @patch.multiple(PostRepository, __abstractmethods__=set())
    @patch.multiple(PostApiGateway, __abstractmethods__=set())
    def _create_mocks_and_dependecies(self, 
        some_tags_saved: List[str], 
        some_posts_from_repository: List[Post], 
        some_posts_from_api: List[Post], 
        some_common_tags: Optional[str], 
        some_new_tags: Optional[str]
        ) -> None:
        self.post_repository: Mock = Mock(PostRepository)
        self.post_repository.get_tags_saved.return_value = some_tags_saved
        self.post_repository.get_posts_by_tag.side_effect = self._get_posts_by_tag
        
        self.post_api_gateway: Mock = Mock(PostApiGateway)
        self.post_api_gateway.get_posts.side_effect = self._get_posts_by_tag


        self.tag_handler: Mock = Mock(TagHandler)
        self.tag_handler.filter_common_tags.return_value = [] if some_common_tags == None else some_common_tags.split(",")
        self.tag_handler.filter_new_tags.return_value = [] if some_new_tags == None else some_new_tags.split(",")

        posts_combined: List[Post] = some_posts_from_repository + some_posts_from_api

        self.post_handler: Mock = Mock(PostHandler)
        self.post_handler.sort_posts.return_value = posts_combined
        self.post_handler.remove_duplicate_posts.return_value = posts_combined

        self.service_application_post: ServiceApplicationPost = ServiceApplicationPost(self.post_api_gateway, self.post_repository, self.tag_handler, self.post_handler)
    
    def _get_posts_by_tag(self, tags: Optional[str]) -> List[Post]:
        results: List[Post] = []

        if tags == None:
            return results
        
        for tag in tags.split(","):
            results.extend(self.SAMPLE_POSTS_BY_TAG.get(tag))
        
        return results
        
    def _create_sample_posts_by_tags(self) -> Dict[str, List[Post]]:
        postBuilder: PostBuilder = PostBuilder()
        samples: Dict[str, List[Post]] = {}

        SOME_POST_TECH: Post = postBuilder.set_id(1).set_author("Alpha").set_author_id(10).set_tags(["tech", "software", "jobs"]).buildPost()
        SOME_POST_DIGITAL_MARKET: Post = postBuilder.set_id(2).set_author("Bravo").set_author_id(20).set_tags(["tech", "Ads", "Web"]).buildPost()
        SOME_POST_CRYPTO: Post = postBuilder.set_id(3).set_author("Charlie").set_author_id(10).set_tags(["tech", "crypto", "NFT", "ETH"]).buildPost()

        SOME_TRAVEL_POST: Post = postBuilder.set_id(4).set_author("Delta").set_author_id(30).set_tags(["food", "travel", "hotel"]).buildPost()
        SOME_FOOD_POST: Post = postBuilder.set_id(5).set_author("Echo").set_author_id(30).set_tags(["food", "garden", "fruits", "vegtables"]).buildPost()

        samples[self.SOME_TECH_TAG] = [SOME_POST_TECH, SOME_POST_DIGITAL_MARKET, SOME_POST_CRYPTO]
        samples[self.SOME_CRYPTO_TAG] = [SOME_POST_CRYPTO]
        samples[self.SOME_TRAVEL_TAG] = [SOME_TRAVEL_POST, SOME_FOOD_POST]

        return samples