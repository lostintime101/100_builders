import React from 'react'
import { useState } from 'react';
import { FaSearch } from "react-icons/fa";
import styles from './SearchBar.module.css';
import { Link, animateScroll as scroll } from 'react-scroll';
import sharedData from './sharedData';

function SearchComponent() {
  const [searchTerm, setSearchTerm] = useState('');
  const [searchResult, setSearchResult] = useState(null);
  const currentAirdrop = sharedData.currentAirdrop;

  const handleSearch = async () => {
    console.log('Search Term:', searchTerm);

  const handleProfileCardClick = (dataObj) => {
  currentAirdrop.groupAddress = dataObj.address;
  currentAirdrop.twitterHandle = dataObj.twitterName;
  console.log("Group address set to: ", currentAirdrop.groupAddress)
  console.log("Twitter Handle set to: ", currentAirdrop.twitterHandle)
  console.log(currentAirdrop)
  };

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
          <div className="profile-picture">
            <Link to="section2" smooth={true} duration={500} onClick={() => handleProfileCardClick(data)}>
              <div className={styles['profile-card']}>
                <img src={data.twitterPfpUrl} alt="Profile Picture" />
                <div className={styles['profile-info']}>
                  <h3>{data.twitterName}</h3>
                  <p><strong>Address:</strong> {formattedAddress}</p>
                  <p><strong>Holder Count:</strong> {data.holderCount}</p>
                </div>
              </div>
            </Link>
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
  <>
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
    </div>
    {searchResult}
 </>
  );
}

export default SearchComponent;

