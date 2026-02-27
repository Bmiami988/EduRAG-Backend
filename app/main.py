from fastapi import FastAPI
from app.services.vectorstore_service import init_vectorstore
from app.api.routes import chat, upload, progress, dev
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.on_event("startup")
def startup():
    init_vectorstore()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # replace with frontend URL later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(chat.router, prefix="/api")
app.include_router(upload.router, prefix="/api")
app.include_router(progress.router, prefix="/api")

# Dev routes (no JWT)
#app.include_router(dev.router, prefix="/dev")

@app.get("/")
def root():

    return {"status": "EduRAG Backend Running"}
