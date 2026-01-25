from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Field, Session, SQLModel, create_engine, select

# 1. UPDATED DATA MODEL
# We added 'content_type' to distinguish between 'movie' and 'series'
# Inside main.py, replace just the 'class Movie' part:

class Movie(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    genre: str
    image: str    # Vertical Poster
    backdrop: str # Horizontal Wallpaper (NEW!)
    trailer: str
    rating: float
    content_type: str = "movie"

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
def home():
    return {"message": "Netflix Clone API is Live!"}

@app.post("/movies")
def create_movie(movie: Movie):
    with Session(engine) as session:
        session.add(movie)
        session.commit()
        session.refresh(movie)
        return movie

@app.get("/movies")
def read_movies():
    with Session(engine) as session:
        movies = session.exec(select(Movie)).all()
        return movies

@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: int):
    with Session(engine) as session:
        movie = session.get(Movie, movie_id)
        if not movie:
            raise HTTPException(status_code=404, detail="Item not found")
        session.delete(movie)
        session.commit()
        return {"ok": True}