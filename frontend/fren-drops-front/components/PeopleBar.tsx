import React, { useState } from 'react';
import { FaEthereum } from "react-icons/fa";
import { BsFillPeopleFill } from "react-icons/bs";
import styles from './AmountBar.module.css';
import sharedData from './sharedData';
import { Link, animateScroll as scroll } from 'react-scroll';

function PeopleBar() {

  const [inputValue, setInputValue] = useState('');
  const currentAirdrop = sharedData.currentAirdrop;
  const max_group_holders = 100;


  const fetchAirdrop = async () => {

      const url = 'http://127.0.0.1:8000/api/v1/drops/';

      const requestBody = {
          creator_address: '0x95222290DD7278Aa3Ddd389Cc1E1d165CC4BAfe5',
          group_address: '0x95222290DD7278Aa3Ddd389Cc1E1d165CC4BAfe5',
          gas_token_amount: 0,
          airdrop_token_amount: currentAirdrop.amount,
          current_token_balance: 0,
          live_for: currentAirdrop.time,
          randomness: currentAirdrop.randomness,
          message: null,
          activated: 'unactivated',
          whitelist_created: false,
          recipients: currentAirdrop.recipients,
          total_addresses_claimed: 0
      };

      const requestOptions = {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(requestBody),
      };

      try {
        const response = await fetch(url, requestOptions);
        if (response.ok) {
          const responseData = await response.json();
          console.log('Response Data:', responseData);
        }
        else {
          const errorResponse = await response.json();
          console.error('Request failed:', response.status, response.statusText);
          console.error('Error Response:', errorResponse);
        }
      }
      catch (error) {
        console.error('Request error:', error);
      }
  };


  const handleAmountChange = () => {

      const updatedInputValue = inputValue.trim();

      if (updatedInputValue !== '') {
        currentAirdrop.recipients = parseInt(updatedInputValue);
        console.log("recipients updated", currentAirdrop.recipients);
      }
      else {
        currentAirdrop.recipients = 1;
        requestBody.recipients = 1;
        console.log("recipients set to 1", currentAirdrop.recipients);
      }
  };

  const handleConfirmClick = async () => {
    handleAmountChange();
    await fetchAirdrop();
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      handleAmountChange();
    }
  };

  return (
    <>
    <div className={styles['search-container']}>
      <BsFillPeopleFill id="FaEthereum" className={styles['search-icon']}/>
      <input
        type="number"
        min="1"
        placeholder={` max ${max_group_holders}`}
        value={inputValue}
        onChange={(e) => setInputValue(e.target.value)}
        onKeyPress={handleKeyPress}
      />
    </div>
      <Link to="section6" smooth={true} duration={500}>
        <button className={styles['button']} onClick={handleConfirmClick}>Confirm</button>
      </Link>
    </>
  );
};

export default PeopleBar;