// components/Search.js
import { useState } from 'react';

function Search() {
  const [searchTerm, setSearchTerm] = useState('');
  const [searchResult, setSearchResult] = useState(null);

  const handleSearch = async () => {
    console.log('Search Term:', searchTerm);
    try {
      const response = await fetch(`http://127.0.0.1:8000/api/v1/group/${searchTerm}`);
      if (response.status === 404) {
        console.error('Twitter handle not found');
        setSearchResult('Twitter handle not found');
        return;
      }

      if (response.ok) {
        const data = await response.json();
        setSearchResult(
          <div>
            <h3>Search Result:</h3>
            <p>Address: {data.address}</p>
            <p>Twitter Username: {data.twitterUsername}</p>
            <p>Twitter Name: {data.twitterName}</p>
            <p>Twitter Profile Picture URL: {data.twitterPfpUrl}</p>
            <p>Twitter User ID: {data.twitterUserId}</p>
          </div>
        );
      } else {
        console.error('Error fetching data');
        setSearchResult('Error fetching data');
      }
    } catch (error) {
      console.error('An error occurred:', error);
      setSearchResult('An error occurred');
    }
  };


  return (
    <div>
      <input
        type="text"
        placeholder="Enter a Twitter handle"
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
      />
      <button onClick={handleSearch}>Search</button>

      {/* Display search result */}
      {searchResult}
    </div>
  );
}

export default Search;
