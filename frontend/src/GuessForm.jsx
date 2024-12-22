import React, { useState } from "react";
import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:8000";

const closeAllLists = () => {
  const lists = document.querySelectorAll(".autocomplete-items");
  lists.forEach((list) => list.remove());
};

const GuessForm = ({ onSubmit }) => {
  const [songTitle, setSongTitle] = useState("");
//   const [searchResults, setSearchResults] = useState([]);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (songTitle.trim()) {
      onSubmit(songTitle);
      setSongTitle("");
    }
  };

  // TODO: change so that it does not post to backend on every change (and does not have to be async function), can just do search locally
  const onChange = async (e) => {
    closeAllLists()
    const inp = e.target.value
    setSongTitle(inp);
    if(inp === "") { 
        // setSearchResults([]); 
        return; 
    }

    // create a div element to contain search items
    const a = document.createElement("DIV");
    a.setAttribute("id", "autocomplete-list");
    a.setAttribute("class", "autocomplete-items");
    try {
      const response = await axios.post(`${API_BASE_URL}/search`, { "title": inp });
    //   setSearchResults(response.data.search);

      response.data.search.forEach((item, index) => {
        // create a DIV element for each matching element
        const b = document.createElement("DIV");
        b.innerHTML = item;

        // Execute function on click of search item
        b.addEventListener("click", function () {
            setSongTitle(this.innerHTML);
            closeAllLists();
        });

        a.appendChild(b);
      });
    } 
    catch (error) {
      console.error("Error on search:", error);
    }
    e.target.parentNode.appendChild(a);
  };

  return (
    <form onSubmit={handleSubmit}>
      <div class="autocomplete" style={{ width:"300px" }}>
        <input
            type="text"
            value={songTitle}
            onInput={onChange}
            placeholder="Enter a song title"
        />
        {/* <div id="autocomplete-list" class="autocomplete-items">
            {searchResults.map((value, index) => (
              <div key={index}>{value}</div>
              ))}
        </div> */}
      </div>
      {/* <input type="submit"> */}
      <button type="submit">Guess</button>
    </form>
  );
};

export { closeAllLists };
export default GuessForm; 
