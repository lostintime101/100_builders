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

  const handleAmountChange = () => {
  if (inputValue !== '') {
    currentAirdrop.recipients = inputValue;
    console.log(currentAirdrop);
  }
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
        <button className={styles['button']} onClick={handleAmountChange}>Confirm</button>
      </Link>
    </>
  );
};

export default PeopleBar;

