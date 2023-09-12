// pages/index.tsx
import { ConnectButton } from '@rainbow-me/rainbowkit';
import type { NextPage } from 'next';
import Head from 'next/head';
import styles from '../styles/Home.module.css';
import { useState } from 'react';
import { Link, animateScroll as scroll } from 'react-scroll';

// components
import SearchComponent from '../components/SearchBar.tsx';
import Header from '../components/Header.tsx';
import AmountBar from '../components/AmountBar.tsx';
import SliderTime from '../components/SliderTime.tsx';
import SliderRandomness from '../components/SliderRandomness.tsx';
import CreateButton1 from '../components/CreateButton1.tsx';
import CreateButton2 from '../components/CreateButton2.tsx';
import CreateButton3 from '../components/CreateButton3.tsx';
import CreateButton4 from '../components/CreateButton4.tsx';
import PeopleBar from '../components/PeopleBar.tsx';
import WaitingDots from '../components/WaitingDots.tsx';

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

      <main2 className={styles.main} id="section2">

        <div className={styles.content}>
        <h1 className={styles.title}>
          Amount to <span className={styles.frendrops}>airdrop</span>
        </h1>
        <AmountBar/>
        <CreateButton1/>
        </div>

      </main2>

      <main3 className={styles.main} id="section3">

        <div className={styles.content}>
        <h1 className={styles.title}>
          Airdrop will be <span className={styles.frendrops}>live</span> for
        </h1>
        <SliderTime/>

        <CreateButton2/>
        </div>

      </main3>

      <main4 className={styles.main} id="section4">

        <div className={styles.content}>
        <h1 className={styles.title}>
          Choose <span className={styles.frendrops}>randomness</span> level
        </h1>
        <SliderRandomness/>

        <CreateButton3/>
        </div>

      </main4>


      <main5 className={styles.main} id="section5">

        <div className={styles.content}>
        <h1 className={styles.title}>
          Drop to ___ <span className={styles.frendrops}>key holders</span>
        </h1>

        <PeopleBar/>
        <CreateButton4/>
        </div>

      </main5>

      <main6 className={styles.main} id="section6">

        <div className={styles.waiting}>
        <h1 className={styles.title}>
          Creating <span className={styles.frendrops}>Fren Drop</span>
        <WaitingDots />
        </h1>
        </div>

      </main6>


      <footer className={styles.footer}>
        <a href="https://rainbow.me" rel="noopener noreferrer" target="_blank">
          Made with ❤️ by fren drops
        </a>
      </footer>
    </div>
  );
};

export default Home;
