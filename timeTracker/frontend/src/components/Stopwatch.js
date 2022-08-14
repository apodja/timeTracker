import React, { useState, useEffect } from 'react';

const Stopwatch = () => {
    const [time, setTime] = useState(0);
    const [running, setRunning] = useState(false);
    useEffect(() => {
      let interval;
      if (running) {
        interval = setInterval(() => {
          setTime((prevTime) => prevTime + 10);
        }, 10);
      } else if (!running) {
        clearInterval(interval);
        if(time > 0){
          send();
          setTime(0);
        }
        
      }
      return () => clearInterval(interval);
    }, [running]);

    function send() {
        const url = "http://127.0.0.1:8000/api/";
        const requestOptions = {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                
            },
            body: JSON.stringify({'ora' : time})
         };
          fetch(url, requestOptions).then((response)=> console.log(response));
    }
    return (
      <div className="stopwatch">
        <div className="digits">
          <span>{("0" + Math.floor((time / 360000) % 60)).slice(-2)}:</span>
          <span>{("0" + Math.floor((time / 60000) % 60)).slice(-2)}:</span>
          <span>{("0" + Math.floor((time / 1000) % 60)).slice(-2)}</span>
        </div>
        <div className="buttons">
          <button className='btn btn-success' onClick={() => setRunning(true)}>Start</button>
          <button className='btn btn-danger' onClick={() => setRunning(false)}>Stop</button>
          {/* <button onClick={() => setTime(0)}>Reset</button> */}
          {/* <button onClick={() => send()}>Send</button> */}
        </div>
      </div>
    );
  };

  export default Stopwatch;