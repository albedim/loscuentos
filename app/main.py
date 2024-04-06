import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request

from app.configuration.config import Base, engine, templates
from app.controller.chapter import chapterRouter
from app.controller.comment import commentRouter
from app.controller.favorite import favoriteRouter
from app.controller.favorite_tag import favoriteTagRouter
from app.controller.interaction import interactionRouter
from app.controller.social_link import socialLinkRouter
from app.controller.story import storyRouter
from app.controller.story_tag import storyTagRouter
from app.controller.tag import tagRouter
from app.controller.user import userRouter

app = FastAPI()
# Qui aggiungiamo telle le nuove rotte presenti nella cartella controller
app.include_router(chapterRouter, prefix="/chapters")
app.include_router(commentRouter, prefix="/comments")
app.include_router(favoriteRouter, prefix="/favorites")
app.include_router(favoriteTagRouter, prefix="/favorite_tags")
app.include_router(interactionRouter, prefix="/interactions")
app.include_router(socialLinkRouter, prefix="/social_links")
app.include_router(storyRouter, prefix="/stories")
app.include_router(storyTagRouter, prefix="/story_tags")
app.include_router(tagRouter, prefix="/tags")
app.include_router(userRouter, prefix="/users")

origins = [
    "http://localhost",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def homepage(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"stories": [1,2,3]}
    )

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    uvicorn.run(app, port=8000)
