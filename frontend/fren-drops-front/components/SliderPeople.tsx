import React, { useEffect, useState } from "react";
import styles from './Slider.module.css';


function SliderPeople() {
    const [data,setData] = useState(50)
    const [description,setDescription] = useState('')
    const [detail,setDetail] = useState('')

    useEffect(()=>{
        if(data == 0){
            setDescription("Few")
            setDetail("First come first served, how many get the drop?")
        }
        else if(data == 25){
            setDescription("Some")
            setDetail("First come first served, how many get the drop?")
        }
        else if(data == 50){
            setDescription("Half")
            setDetail("First come first served, how many get the drop?")
        }
        else if(data == 75){
            setDescription("Most")
            setDetail("First come first served, how many get the drop?")
        }
        else if(data == 100){
            setDescription("All")
            setDetail("First come first served, how many get the drop?")
        }
    },[data])

    return(
        <>
        <div className={styles['slider-container']}>
            <p className={styles['slider-title']}>Holders</p>
            <input className={styles['slider']} type="range" min="0" max="100" step="25" value={data} onChange={(e)=>setData(e.target.value)} />
            <p className={styles['slider-status']}>{description}</p>
        </div>
        <p className={styles['slider-detail']}>{detail}</p>
        </>
    );
}
export default SliderPeople;