from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, ConfigDict
from data import songs, get_songs
from contextlib import asynccontextmanager
from game import Game
from song import Song
import re
"""
This file creates API endpoints for the backend at which the frontend can post user inputs and receive results
"""


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load songs when the API starts.
    get_songs()
    yield

app = FastAPI(lifespan=lifespan)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React app origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Global variables for the game
game_active = False
game = None


# Models for request and response
class SearchRequest(BaseModel):
    title: str


class SearchResponse(BaseModel):
    search: list[str] = []


class GuessRequest(BaseModel):
    songTitle: str


class GuessResponse(BaseModel):
    song_found: dict
    correct: bool
    guesses: int
    colors: str


class StartGameResponse(BaseModel):
    targetHint: str


@app.post("/start_game", response_model=StartGameResponse)
def start_game():
    """
    Start a new game by selecting a random target song.
    """
    global game_active, game
    game = Game()
    game_active = True

    return StartGameResponse(targetHint="The game has started! Guess the song title.")


@app.post("/search", response_model=SearchResponse)
def search(input: SearchRequest):
    """
    Handle a player's guess.
    """
    global game_active

    if not game_active:
        raise HTTPException(status_code=400, detail="No active game. Start a new game first.")

    song_title = input.title
    search = []

    # Search for the guessed song in the songs list
    for song in songs:
        if re.search(song_title, song.title, re.IGNORECASE):
            search.append(song.title)

    return SearchResponse(search=search)


@app.get("/test")
def test():
    # assess if posting an arbitrary object works
    return Song("STARGAZING", 4, 1, "4:30", [])


@app.post("/make_guess", response_model=GuessResponse)
def make_guess(guess: GuessRequest):
    """
    Handle a player's guess.
    """
    global game, game_active
    if not game_active:
        raise HTTPException(status_code=400, detail="No active game. Start a new game first.")

    song_title = guess.songTitle
    stat_str, num_guesses, solved, song_hit = game.guess(song_title)

    return GuessResponse(
        song_found=song_hit.dict() if song_hit else {},
        correct=solved,
        guesses=num_guesses,
        colors=stat_str,
    )


# Likely not needed
@app.post("/end_game")
def end_game():
    """
    End the current game.
    """
    global game_active
    if not game_active:
        raise HTTPException(status_code=400, detail="No active game to end.")

    game_active = False
    return {"message": "You did it!"}