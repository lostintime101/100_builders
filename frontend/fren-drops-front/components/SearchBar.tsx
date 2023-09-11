import React from 'react'
import { useState } from 'react';
import { FaSearch } from "react-icons/fa";
import styles from './SearchBar.module.css';

function SearchComponent() {
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
        const ethereumAddress = data.address;
        const firstFive = ethereumAddress.slice(0, 4);
        const lastFive = ethereumAddress.slice(-4);
        const formattedAddress = `${firstFive}...${lastFive}`;

        setSearchResult(

          <div className="profile-card">
            <a href="#amount-section" className="profile-card">
            <div className="profile-picture">
              <img src={data.twitterPfpUrl} alt="Profile Picture" />
            </div>
            <div className="profile-info">
              <h3>{data.twitterName}</h3>
              <p><strong>Address:</strong> {formattedAddress}</p>
              <p><strong>Holder Count:</strong> {data.holderCount}</p>
            </div>
            </a>
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
    <div className={styles['search-container']}>
      <FaSearch id="search-icon" className={styles['search-icon']}/>
      <input
        type="text"
        placeholder="paste a Twitter handle ..."
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
        onKeyPress={(e) => {
          if (e.key === 'Enter') {
            handleSearch();
          }
        }}
      />
      <div className="search-result">
        {searchResult}
      </div>
    </div>
  );
}

export default SearchComponent;

