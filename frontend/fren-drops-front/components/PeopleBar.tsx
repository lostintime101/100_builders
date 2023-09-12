import React from 'react'
import { FaEthereum } from "react-icons/fa";
import { BsFillPeopleFill } from "react-icons/bs";
import styles from './AmountBar.module.css';

function PeopleBar() {
  const max_group_holders = 100;
  return (
    <>
    <div className={styles['search-container']}>
      <BsFillPeopleFill id="FaEthereum" className={styles['search-icon']}/>
      <input
        type="number"
        min="1"
        placeholder={` max ${max_group_holders}`}
        onKeyPress={(e) => {
          if (e.key === 'Enter') {
            console.log("amount of ETH to airdrop entered");
          }
        }}
      />
    </div>
    </>
  );
};

export default PeopleBar;

