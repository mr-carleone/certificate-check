from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router
from app.config.settings import settings
from app.core.logging import logger

app = FastAPI(title=settings.APP_NAME)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

if __name__ == "__main__":
    import uvicorn

    logger.info("Starting Certificate Manager API")
    uvicorn.run(app, host="0.0.0.0", port=8000)
