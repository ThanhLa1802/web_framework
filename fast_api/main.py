from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
posts = [
    {
        "id": 1,
        "author": "Thanh La",
        "title": "What's is FastAPI",
        "content": "Fast API is really easy to build your web application",
        "date_posted": "January 19, 2026"
    }, 
    {
        "id": 2,
        "author": "Thanh La",
        "title": "What's is FastAPI",
        "content": "Fast API is really easy to build your web application",
        "date_posted": "January 19, 2026"
    }
]

@app.get("/", response_class=HTMLResponse, include_in_schema=False)
@app.get("/posts", response_class=HTMLResponse, include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(
        request,
        "home.html",
        {"posts": posts, "title": "Home"}
    )

@app.get("/api/posts")
def get_posts():
    return posts