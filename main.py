from fastapi import FastAPI
from app.v1.routers.user_router import router as user_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

ALLOWED_HOSTS = [
    "http://localhost",
    "http://localhost:4200",
]

if not ALLOWED_HOSTS:
    ALLOWED_HOSTS = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user_router)

