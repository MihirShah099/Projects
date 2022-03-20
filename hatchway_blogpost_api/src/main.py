from src.Ressources import postRessources, pingRessources
from fastapi import FastAPI, status, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


app = FastAPI()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    message: str = None

    if ("tags" in str(exc)):
        message = "Tags parameter is required"
    elif ("sortBy" in str(exc)):
        message = "sortBy parameter is invalid"
    else:
        message = "direction parameter is invalid"

    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content= {"error": message})

app.include_router(postRessources.posts_router)
app.include_router(pingRessources.ping_router)