from src.Domain.Post.postsHandler import PostHandler
from src.Domain.Tag.tagHandler import TagHandler
from src.Domain.Post.postRepository import PostRepository
from src.Domain.Post.post import Post
from src.Domain.Post.postApiGateway import PostApiGateway
from typing import List, Optional


class ServiceApplicationPost:
    def __init__(self, post_api_gateway: PostApiGateway, post_repository: PostRepository, tag_handler: TagHandler,
                 posts_handler: PostHandler) -> None:
        self.post_api_gateway = post_api_gateway
        self.post_repository = post_repository
        self.tag_handler = tag_handler
        self.posts_handler = posts_handler

    def get_posts(self, tags: str, sort_by: Optional[str], direction: Optional[str]) -> List[Post]:
        posts: List[Post] = []

        saved_tags: List[str] = self.post_repository.get_tags_saved()

        new_tags: List[str] = self.tag_handler.filter_new_tags(tags, saved_tags)
        existed_tags: List[str] = self.tag_handler.filter_common_tags(tags, saved_tags)

        posts.extend(self._get_posts_from_external_service(new_tags))
        posts.extend(self._get_post_from_memory(existed_tags))

        posts = self.posts_handler.remove_duplicate_posts(posts)
        posts = self.posts_handler.sort_posts(posts, sort_by, direction)

        return posts

    def _get_posts_from_external_service(self, tags: List[str]) -> List[Post]:
        posts: List[Post] = []

        for tag in tags:
            result: List[Post] = self.post_api_gateway.get_posts(tag)
            self.post_repository.save_posts(tag, result)
            posts.extend(result)

        return posts

    def _get_post_from_memory(self, tags: List[str]) -> List[Post]:
        posts: List[Post] = []

        for tag in tags:
            posts.extend(self.post_repository.get_posts_by_tag(tag))

        return posts

