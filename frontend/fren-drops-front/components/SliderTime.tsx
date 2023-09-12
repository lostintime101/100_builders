import React, { useEffect, useState } from "react";
import styles from './Slider.module.css';


function SliderTime() {
    const [data,setData] = useState(50)
    const [description,setDescription] = useState('')
    const [detail,setDetail] = useState('')

    useEffect(()=>{
        if(data == 0){
            setDescription("24 hrs")
            setDetail(`I gave you an entire day to claim bro.`)
        }
        else if(data == 25){
            setDescription("18 hrs")
            setDetail(`You really need to check the chat more often.`)
        }
        else if(data == 50){
            setDescription("12 hrs")
            setDetail(`Ample time to claim.`)
        }
        else if(data == 75){
            setDescription("6 hrs")
            setDetail(`You were sleeping? Sorry`)
        }
        else if(data == 100){
            setDescription("1 hr")
            setDetail(`Having lunch? NGMI`)
        }
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
export default SliderTime;