from src.Domain.Tag.tagHandler import TagHandler
from typing import List
import unittest

class TagTest(unittest.TestCase):

    def setUp(self) -> None:
        self.SOME_TAGS_SAVED: List[str] = ["tech", "music", "history"]
        
    def test_given_string_with_some_same_tags_with_saved_tags_when_filtering_common_tags_then_same_tags_between_string_and_saved_tags_are_returned(self):
        SOME_TAGS: str = "history,culture,science,music"


        common_tags: List[str] = TagHandler().filter_common_tags(SOME_TAGS, self.SOME_TAGS_SAVED)
        
        expected_common_tags: List[str] = sorted(["history", "music"])
        self.assertCountEqual(expected_common_tags, common_tags)
        self.assertListEqual(expected_common_tags, sorted(common_tags))

    def test_given_string_with_no_same_tags_with_saved_tags_when_filtering_common_tags_then_empty_list_is_returned(self):
        SOME_TAGS: str = "travel,politics"

        tags: List[str] = TagHandler().filter_common_tags(SOME_TAGS, self.SOME_TAGS_SAVED)

        self.assertCountEqual([], tags)
        self.assertListEqual([], tags)  

    def  test_given_string_with_some_same_tags_with_saved_tags_when_filtering_new_tags_then_same_tags_between_string_and_saved_tags_are_returned(self):
        SOME_TAGS: str = "history,science,music,food,travel"

        different_tags: List[str] = TagHandler().filter_new_tags(SOME_TAGS, self.SOME_TAGS_SAVED)

        expected_different_tags: List[str] = sorted(["science", "food", "travel"])
        self.assertCountEqual(expected_different_tags, different_tags)
        self.assertListEqual(expected_different_tags, sorted(different_tags))
    

    def test_given_string_with_no_same_tags_with_saved_tags_when_filtering_new_tags_then_empty_list_is_returned(self):
        SOME_TAGS: str = ",".join(self.SOME_TAGS_SAVED)

        tags: List[str] = TagHandler().filter_new_tags(SOME_TAGS, self.SOME_TAGS_SAVED)

        self.assertCountEqual([], tags)
        self.assertListEqual([], tags)  