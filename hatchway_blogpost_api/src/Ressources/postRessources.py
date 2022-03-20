from src.Configurations.configurations import Configurations
from src.ServiceApplications.ServiceApplicationsPost import ServiceApplicationPost
from fastapi import APIRouter, Query
from typing import Optional

from src.Domain.Post.directionsValues import DirectionsValues
from src.Domain.Post.sortByValues import SortByValues

posts_router: APIRouter = APIRouter()
_service_application_post: ServiceApplicationPost = Configurations().get_service_application_post()

@posts_router.get("/api/posts")
def get_posts(
    tags: str = Query(..., title="Tags", description="Each tag must be seperated by a comma."), 
    sortBy: Optional[SortByValues] = Query(None, title="Sort by", description="The field to sort the posts by."), 
    direction: Optional[DirectionsValues] = Query(None, title = "Direction", description="The direction for sorting.")
    ):
    return {"posts": _service_application_post.get_posts(tags, sortBy, direction)}