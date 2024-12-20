import React from "react";

const GuessList = ({ guessList = [] }) => {
  if (guessList.length == 0) {
    return null;
  }
//   console.log(guessList[0].song.title)

  return (
    <div>
      <h3>Guesses</h3>
        <table>
          <thead>
            <tr>
              <th>Song</th>
              <th>Album</th>
              <th>Track No.</th>
              <th>Track Length</th>
              <th>Features</th>
              <th>Colors</th>
            </tr>
          </thead>
          {guessList.map((guess) => (
          <tbody>
            <tr>
              <td>{guess.song.title}</td>
              <td>{guess.song.album}</td>
              <td>{guess.song.number}</td>
              <td>{guess.song.length}</td>
              <td>{guess.song.features}</td>
              <td>{guess.colors}</td>
            </tr>
          </tbody>))}
        </table>
    </div>
  );
};

export default GuessList;