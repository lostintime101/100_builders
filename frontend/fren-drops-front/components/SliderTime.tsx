import React, { useEffect, useState } from "react";
import styles from './Slider.module.css';


function SliderTime() {
    const [data,setData] = useState(50)
    const [description,setDescription] = useState('')
    const [detail,setDetail] = useState('')

    useEffect(()=>{
        if(data == 0){
            setDescription("24 hrs")
            setDetail(`After which unclaimed funds will be returned.`)
        }
        else if(data == 25){
            setDescription("18 hrs")
            setDetail(`After which unclaimed funds will be returned.`)
        }
        else if(data == 50){
            setDescription("12 hrs")
            setDetail(`After which unclaimed funds will be returned.`)
        }
        else if(data == 75){
            setDescription("6 hrs")
            setDetail(`After which unclaimed funds will be returned.`)
        }
        else if(data == 100){
            setDescription("1 hr")
            setDetail(`After which unclaimed funds will be returned.`)
        }
    },[data])

    return(
        <>
        <div className={styles['slider-container']}>
            <p className={styles['slider-title']}>Time</p>
            <input className={styles['slider']} type="range" min="0" max="100" step="25" value={data} onChange={(e)=>setData(e.target.value)} />
            <p className={styles['slider-status']}>{description}</p>
        </div>
        <p className={styles['slider-detail']}>{detail}</p>
        </>
    );
}
export default SliderTime;