// no longer necessary if GuessForm autocompletion works
import React from "react";

const SearchResults = ({ results = [] }) => {
  if (results.length == 0) {
    return null;
  }

  return (
    <div>
      <h3>Search Results</h3>
      <ul>
        {results.map((result, index) => (
          <li key={index}>{result}</li>
        ))}
      </ul>
    </div>
  );
};

export default SearchResults;