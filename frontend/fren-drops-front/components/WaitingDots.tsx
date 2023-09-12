import React, { useEffect, useState } from 'react';

function WaitingDots() {
  const [dots, setDots] = useState(''); // Initialize with an empty string

  useEffect(() => {
    const interval = setInterval(() => {
      setDots((prevDots) => (prevDots.length === 3 ? '' : prevDots + '.'));
    }, 500); // Adjust the interval to control animation speed

    return () => clearInterval(interval); // Cleanup on unmount
  }, []);

  return <div className="loading-dots">{dots}</div>;
}

export default WaitingDots;
