import React from 'react';
import { ConnectButton } from '@rainbow-me/rainbowkit';
import styles from './Header.module.css';

export default function SearchBar() {
  return (
    <div className={styles.header}>
      <ConnectButton chainStatus="icon" />
    </div>
  );
}
