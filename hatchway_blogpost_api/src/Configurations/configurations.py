
from src.Domain.Post.postsHandler import PostHandler
from src.Domain.Tag.tagHandler import TagHandler
from src.ServiceApplications.ServiceApplicationsPost import ServiceApplicationPost
from src.Infrastructure.Persistence.PostsInMemory import PostsInMemory
from src.Domain.Post.postRepository import PostRepository
from src.Infrastructure.External.hatchwaysApi import HatchwaysApi
from src.Domain.Post.postApiGateway import PostApiGateway


class Configurations:
    def __init__(self) -> None:
        post_api_gateway: PostApiGateway = HatchwaysApi()
        post_repository: PostRepository = PostsInMemory()
        self.service_application_post: ServiceApplicationPost = ServiceApplicationPost(post_api_gateway, post_repository, TagHandler(), PostHandler())

    def get_service_application_post(self) -> ServiceApplicationPost:
        return self.service_application_post