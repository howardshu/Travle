import React from "react";
import "./styles.css";

const colorMap = {
    'G': "green",
    'U': "yellow",
    'D': "yellow",
    'H': "black",
    'L': "black",
    'B': "black",
    'Y': "yellow"
}

const arrowMap = {
    'G': "",
    'U': " ↑",
    'D': " ↓",
    'H': " ↑",
    'L': " ↓",
    'B': "",
    'Y': ""
}

const GuessList = ({ guessList = [] }) => {
  if (guessList.length == 0) {
    return null;
  }
  console.log(colorMap['G'])
  // TODO: implement guessList as a static variable so don't have to loop through whole list each time
  return (
    <div>
      <h3>Guesses</h3>
        <table style={{ width: 1500 }}>
          <thead>
            <tr>
              <th>Song</th>
              <th>Album</th>
              <th>Track No.</th>
              <th>Track Length</th>
              <th>Features</th>
            </tr>
          </thead>
          {guessList.map((guess, rowIndex) => (
            <tbody>
            <tr key={rowIndex}>
              {Object.values(guess.song).map((value, colIndex) => (
                <td key={colIndex} style={{ backgroundColor: colorMap[guess.colors[colIndex]] }}>{value}{arrowMap[guess.colors[colIndex]]}</td>
              ))}
            </tr>
          </tbody>))}
        </table>
    </div>
  );
};

export default GuessList;