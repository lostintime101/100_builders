import React, { useEffect, useState } from "react";
import styles from './Slider.module.css';
import sharedData from './sharedData';


function SliderTime() {
    const [data,setData] = useState(50)
    const [description,setDescription] = useState('')
    const [detail,setDetail] = useState('')
    const currentAirdrop = sharedData.currentAirdrop;

    useEffect(()=>{
        if(data == 0){
            setDescription("24 hrs")
            setDetail(`I gave you an entire day to claim bro.`)
            currentAirdrop.time = 24;
        }
        else if(data == 25){
            setDescription("18 hrs")
            setDetail(`You really need to check the chat more often.`)
            currentAirdrop.time = 18;
        }
        else if(data == 50){
            setDescription("12 hrs")
            setDetail(`Ample time to claim.`)
            currentAirdrop.time = 12;
        }
        else if(data == 75){
            setDescription("6 hrs")
            setDetail(`You were sleeping? Sorry`)
            currentAirdrop.time = 6;
        }
        else if(data == 100){
            setDescription("1 hr")
            setDetail(`Having lunch? NGMI`)
            currentAirdrop.time = 1;
        }
        console.log(currentAirdrop.time);
    },[data])

    return(
        <>
        <h1 className={styles['slider-status']}>{description}</h1>
        <div className={styles['slider-container']}>
            <input className={styles['slider']}
            type="range"
            min="0"
            max="100"
            step="25"
            value={data}
            onChange={(e)=>setData(e.target.value)}
        />
        </div>
        <p className={styles['slider-detail']}>{detail}</p>
        </>
    );
}
export default SliderTime;