from fastapi.routing import APIRouter

ping_router: APIRouter = APIRouter()

@ping_router.get("/api/ping")
def ping():
    return {"success": True}