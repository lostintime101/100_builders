import React, { useEffect, useState } from "react";
import styles from './Slider.module.css';
import sharedData from './sharedData';


function SliderRandomness() {
    const [data,setData] = useState(50)
    const [description,setDescription] = useState('')
    const [detail,setDetail] = useState('')
    const currentAirdrop = sharedData.currentAirdrop;

    useEffect(()=>{
        if(data == 0){
            setDescription("None")
            setDetail("All are equal here comrade")
            currentAirdrop.randomness = "None";
        }
        else if(data == 25){
            setDescription("Low")
            setDetail("Rewards mildly randomized")
            currentAirdrop.randomness = "Low";
        }
        else if(data == 50){
            setDescription("Medium")
            setDetail("Airdrop rewards are randomized normally")
            currentAirdrop.randomness = "Medium";
        }
        else if(data == 75){
            setDescription("High")
            setDetail("Highly randomized rewards")
            currentAirdrop.randomness = "High";
        }
        else if(data == 100){
            setDescription("Degen")
            setDetail("Outright degenerate levels of randomness")
            currentAirdrop.randomness = "Degen";
        }
        console.log(currentAirdrop.randomness);
    },[data])

    return(
        <>
        <h1 className={styles['slider-status']}>{description}</h1>
        <div className={styles['slider-container']}>
            <input className={styles['slider']} type="range" min="0" max="100" step="25" value={data} onChange={(e)=>setData(e.target.value)} />
        </div>
        <p className={styles['slider-detail']}>{detail}</p>
        </>
    );
}
export default SliderRandomness;