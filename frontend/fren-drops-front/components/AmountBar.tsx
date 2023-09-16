import React, { useState } from 'react';
import { FaEthereum } from "react-icons/fa";
import styles from './AmountBar.module.css';
import sharedData from './sharedData';
import { Link, animateScroll as scroll } from 'react-scroll';

function AmountBar() {
  const [inputValue, setInputValue] = useState('');
  const currentAirdrop = sharedData.currentAirdrop;

  const handleAmountChange = () => {
  if (inputValue !== '') {
    currentAirdrop.amount = parseInt(inputValue);
    console.log("Amount", currentAirdrop.amount);
  }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      handleAmountChange();
    }
  };

  return (
    <div className={styles['search-container']}>
      <FaEthereum id="FaEthereum" className={styles['search-icon']}/>
      <input
        type="number"
        min="0.001"
        placeholder="eth..."
        value={inputValue}
        onChange={(e) => setInputValue(e.target.value)}
        onKeyPress={handleKeyPress}
      />
      <Link to="section3" smooth={true} duration={500}>
      <button onClick={handleAmountChange}>Confirm</button>
      </Link>
    </div>

  );
};

export default AmountBar;

