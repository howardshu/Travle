from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from data import songs, get_songs
from contextlib import asynccontextmanager
import random
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
target = None  # Target song for the current game
game_active = False


# Models for request and response
class SearchRequest(BaseModel):
    title: str


class SearchResponse(BaseModel):
    search: list[str] = []


class GuessRequest(BaseModel):
    songTitle: str


class GuessResponse(BaseModel):
    song_found: bool
    correct: bool
    colors: str


class StartGameResponse(BaseModel):
    targetHint: str


@app.post("/start_game", response_model=StartGameResponse)
def start_game():
    """
    Start a new game by selecting a random target song.
    """
    global target, game_active
    target = random.choice(songs)  # Choose a random song
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


@app.post("/make_guess", response_model=GuessResponse)
def make_guess(guess: GuessRequest):
    """
    Handle a player's guess.
    """
    global target, game_active

    if not game_active:
        raise HTTPException(status_code=400, detail="No active game. Start a new game first.")

    song_title = guess.songTitle
    song_hit = None
    # search = []

    # Search for the guessed song in the songs list
    for song in songs:
        if song.title == song_title:
            song_hit = song
            break
        # elif re.search(song_title, song.title, re.IGNORECASE):
        #     search.append(song.title)

    if song_hit is not None:
        # Check if the guessed song matches the target
        correct, stat_str = target.check_match(song_hit)
        if correct:
            game_active = False  # End the game if the guess is correct
        return GuessResponse(
            song_found=True,
            correct=correct,
            colors=stat_str
        )
    else:
        return GuessResponse(
            song_found=False,
            correct=False,
            colors=""
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