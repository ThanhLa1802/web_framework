from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
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
def home():
    return f"<h1>Welcome to the Blog Home Page</h1><p>Number of posts: {len(posts)}</p>"

@app.get("/api/posts")
def get_posts():
    return posts