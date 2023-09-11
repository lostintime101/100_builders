import React from 'react'
import { FaEthereum } from "react-icons/fa";
import styles from './AmountBar.module.css';

function AmountBar() {
  return (
    <div className={styles['search-container']}>
      <FaEthereum id="FaEthereum" className={styles['search-icon']}/>
      <input
        type="number"
        min="0.001"
        placeholder="eth..."
        onKeyPress={(e) => {
          if (e.key === 'Enter') {
            console.log("amount of ETH to airdrop entered");
          }
        }}
      />
    </div>
  );
};

export default AmountBar;

