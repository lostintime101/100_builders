// pages/index.tsx
import { ConnectButton } from '@rainbow-me/rainbowkit';
import type { NextPage } from 'next';
import Head from 'next/head';
import styles from '../styles/Home.module.css';
import SearchComponent from '../components/SearchBar.tsx';
import Header from '../components/Header.tsx';
import { useState } from 'react';

const Home: NextPage = () => {

  const [amount, setAmount] = useState('');

  const handleConfirm = () => {
    // Store the amount or use it as needed.
    console.log('Confirmed Amount:', amount);
  };

  return (
    <div className={styles.container}>
      <Head>
        <title>Fren Drops</title>
        <meta
          content="Welcome to Fren Drops"
          name="description"
        />
        <link href="/favicon.ico" rel="icon" />
      </Head>
      <Header />
      <main className={styles.main}>


        <h1 className={styles.title}>
          Welcome to <a href="">Fren Drops</a>
        </h1>

        <SearchComponent />
      </main>

      <div id="amount-section" className={styles.amountSection}>
        <input
          type="number"
          placeholder="Enter Amount"
          value={amount}
          onChange={(e) => setAmount(e.target.value)}
        />
        <button onClick={handleConfirm}>Confirm</button>
      </div>

      <footer className={styles.footer}>
        <a href="https://rainbow.me" rel="noopener noreferrer" target="_blank">
          Made with ❤️ by fren drops
        </a>
      </footer>
    </div>
  );
};

export default Home;
