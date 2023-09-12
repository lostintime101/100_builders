import React, { useEffect, useState } from "react";
import styles from './CreateButton.module.css';
import { Link, animateScroll as scroll } from 'react-scroll';

function CreateButton3() {

    return(
        <div className={styles.createButton}>
            <Link to="section5" smooth={true} duration={500}>
            <button className={styles.button}>Confirm</button>
            </Link>
        </div>
    );
}
export default CreateButton3;

