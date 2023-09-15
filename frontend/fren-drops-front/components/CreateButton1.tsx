import React, { useEffect, useState } from "react";
import styles from './CreateButton.module.css';
import { Link, animateScroll as scroll } from 'react-scroll';
import sharedData from './sharedData';

function CreateButton1() {
    const currentAirdrop = sharedData.currentAirdrop;

    return(
        <div className={styles.createButton}>
            <Link to="section3" smooth={true} duration={500}>
            <button className={styles.button}>Confirm</button>
            </Link>
        </div>
    );
}
export default CreateButton1;

