from typing import List, Set

class TagHandler:
    def filter_common_tags(self, tags: str, saved_tags:List[str]) -> List[str]:
        itemsoftags: Set[str] = set(tags.split(","))
        return list(set(saved_tags).intersection(itemsoftags))

    def filter_new_tags(self, tags: str, saved_tags: List[str]) -> List[str]:
        itemsoftags: Set[str] = set(tags.split(","))
        return list(itemsoftags.difference(saved_tags))
