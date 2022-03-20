
from src.Domain.Post.post import Post
from src.Domain.Post.directionsValues import DirectionsValues
from src.Domain.Post.sortByValues import SortByValues
from typing import List, Optional

class PostHandler:
    
    def sort_posts(self, posts: List[Post], sort_by: Optional[str], direction: Optional[str]) -> List[Post]:
        is_ascending: bool = False if direction == None or direction == DirectionsValues.asc else True
        key_value: str = SortByValues.id if sort_by == None else sort_by

        return sorted(posts, key=lambda post: post.dict().get(key_value), reverse=is_ascending)
    
    def remove_duplicate_posts(self, posts: List[Post]) -> List[Post]:
        return list(set(posts))