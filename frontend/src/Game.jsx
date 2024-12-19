import React, { useState } from "react";
import axios from "axios";
import GuessForm from "./GuessForm";
import SearchResults from "./SearchResults";

const API_BASE_URL = "http://127.0.0.1:8000"; // Replace with your backend URL

const Game = () => {
  const [gameStarted, setGameStarted] = useState(false);
  const [solved, setSolved] = useState(false);
  const [valid, setValid] = useState(true); // TODO: add warning about invalid guess
  const [colors, setColors] = useState("");
  const [search, setSearch] = useState([]);
  const [guess, setGuess] = useState("");
  const [message, setMessage] = useState("");

  const startGame = async () => {
    try {
      const response = await axios.post(`${API_BASE_URL}/start_game`);
      setGameStarted(true);
      setColors("");
      setSearch([]);
      setMessage("The game has started! Guess the song.")
    } catch (error) {
      console.error("Error starting game:", error);
      setMessage("Failed to start the game. Try again.");
    }
  };

  const submitGuess = async (songTitle) => {
    try {
      const response = await axios.post(`${API_BASE_URL}/make_guess`, { "songTitle": songTitle });
      setSolved(response.data.song_found);
      setSolved(response.data.correct);
      setColors(response.data.colors);

      if (response.data.correct) {
        setGameStarted(false); // TODO: optimize to show congratulations screen before ending the game
      }
    } catch (error) {
      console.error("Error making a guess:", error);
      setMessage("Failed to submit your guess. Try again.");
    }
  };

  const doSearch = async (title) => {
    try {
      const response = await axios.post(`${API_BASE_URL}/search`, { "title": title });
      setSearch(response.data.search);
    } catch (error) {
      console.error("Error on search:", error);
      setMessage("Failed to search. Try again.");
    }
  };

  return (
    <div>
      <h1>TRAVLE</h1>
      <p>{message}</p>
      {!gameStarted ? (
        <button onClick={startGame}>Start Game</button>
      ) : (
        <>
          <GuessForm onSubmit={submitGuess} />
          <SearchResults searchResults={search} />
          <p>Colors={colors}</p>
        </>
      )}
    </div>
  );
};

export default Game;
