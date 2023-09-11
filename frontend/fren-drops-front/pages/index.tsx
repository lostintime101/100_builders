// pages/index.tsx
import { ConnectButton } from '@rainbow-me/rainbowkit';
import type { NextPage } from 'next';
import Head from 'next/head';
import styles from '../styles/Home.module.css';
import { useState } from 'react';

// components
import SearchComponent from '../components/SearchBar.tsx';
import Header from '../components/Header.tsx';
import AmountBar from '../components/AmountBar.tsx';
import SliderPeople from '../components/SliderPeople.tsx';
import SliderTime from '../components/SliderTime.tsx';
import SliderRandomness from '../components/SliderRandomness.tsx';


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

        <div className={styles.content}>
        <h1 className={styles.title}>
          Welcome to <span className={styles.frendrops}>Fren Drops</span>
        </h1>
        <SearchComponent />
        </div>

      </main>

      <main2 className={styles.main}>

        <div className={styles.content}>
        <h1 className={styles.title}>
          Amount to <span className={styles.frendrops}>airdrop</span>
        </h1>
        <AmountBar/>
        </div>

      </main2>

      <main3 className={styles.main}>

        <div className={styles.content}>
        <h1 className={styles.title}>
          Choose your <span className={styles.frendrops}>settings</span>
        </h1>
        <SliderTime/>
        <SliderPeople/>
        <SliderRandomness/>

        </div>

      </main3>

      <main4 className={styles.main}>



      </main4>


      <footer className={styles.footer}>
        <a href="https://rainbow.me" rel="noopener noreferrer" target="_blank">
          Made with ❤️ by fren drops
        </a>
      </footer>
    </div>
  );
};

export default Home;
