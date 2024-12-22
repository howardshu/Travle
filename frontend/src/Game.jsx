import React, { useState } from "react";
import axios from "axios";
import GuessForm, { closeAllLists } from "./GuessForm";
import SearchResults from "./SearchResults";
import GuessList from "./GuessList";
import "./styles.css";

const API_BASE_URL = "http://127.0.0.1:8000";

const Game = () => {
  const [gameStarted, setGameStarted] = useState(false);
  const [solved, setSolved] = useState(false);
  // const [valid, setValid] = useState(true); // TODO: add warning about invalid guess
  // const [colors, setColors] = useState("");
  // const [search, setSearch] = useState([]);
  const [guesses, setGuesses] = useState(0)
  const [guessList, setGuessList] = useState([]);
  // const [guess, setGuess] = useState("");
  const [message, setMessage] = useState("");

  const startGame = async () => {
    try {
      const response = await axios.post(`${API_BASE_URL}/start_game`);
      closeAllLists()
      setGameStarted(true);
      setSolved(false)
      // setSearch([]);
      setGuesses(0);
      setGuessList([]);
      setMessage("The game has started! Guess the song.")
    } catch (error) {
      console.error("Error starting game:", error);
      setMessage("Failed to start the game. Try again.");
    }
  };

  const submitGuess = async (songTitle) => {
    try {
      const response = await axios.post(`${API_BASE_URL}/make_guess`, { "songTitle": songTitle });
      setSolved(response.data.correct);
      setGuesses(response.data.guesses);
      // setColors(response.data.colors);

      if(Object.keys(response.data.song_found).length > 0) {
        setGuessList([...guessList, {song: response.data.song_found, colors: response.data.colors}]);
      }

      // if (response.data.correct) {
      //   setGameStarted(false); // TODO: optimize to show congratulations screen before ending the game
      // }
    } catch (error) {
      console.error("Error making a guess:", error);
      setMessage("Failed to submit your guess. Try again.");
    }
  };

  // no longer necessary if GuessForm autocompletion works
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
          Number of guesses: {guesses}/8
          <GuessList guessList={guessList} />
        </>
      )}
      {solved ? (
        <> 
        You did it! 
        <button onClick={startGame}>Start a new game</button>
        </>
      ) : null}
    </div>
  );
};

export default Game;
