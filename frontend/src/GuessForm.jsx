import React, { useState } from "react";

const GuessForm = ({ onSubmit }) => {
  const [songTitle, setSongTitle] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (songTitle.trim()) {
      onSubmit(songTitle);
      setSongTitle("");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={songTitle}
        onChange={(e) => setSongTitle(e.target.value)}
        placeholder="Enter a song title"
      />
      <button type="submit">Guess</button>
    </form>
  );
};

export default GuessForm;
