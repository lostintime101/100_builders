import React, { useEffect, useState } from "react";
import styles from './Slider.module.css';


function SliderRandomness() {
    const [data,setData] = useState(50)
    const [description,setDescription] = useState('')
    const [detail,setDetail] = useState('')

    useEffect(()=>{
        if(data == 0){
            setDescription("None")
            setDetail("All are equal here comrade")
        }
        else if(data == 25){
            setDescription("Low")
            setDetail("Mild randomization")
        }
        else if(data == 50){
            setDescription("Mid")
            setDetail("Randomized amounts")
        }
        else if(data == 75){
            setDescription("High")
            setDetail("Risk addict")
        }
        else if(data == 100){
            setDescription("Degen")
            setDetail("Outright degenerate level of randomness")
        }
    },[data])

    return(
        <>
        <div className={styles['slider-container']}>
            <p className={styles['slider-title']}>Randomness</p>
            <input className={styles['slider']} type="range" min="0" max="100" step="25" value={data} onChange={(e)=>setData(e.target.value)} />
            <p className={styles['slider-status']}>{description}</p>
        </div>
        <p className={styles['slider-detail']}>{detail}</p>
        </>
    );
}
export default SliderRandomness;