'use client';
import Timer, { TimerHandle } from './components/Timer';
import Display, { DisplayHandle } from './components/Display';
import { useRef, useState, useEffect } from 'react';
import axios from 'axios';

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.withCredentials = true;

const client = axios.create({
  baseURL: 'http://backend-service:8000'
});

const sendPing = () => {
  axios.get('/health').then(response => {console.log(response)}).catch(error => {console.error('Error fetching authentication status:', error);});
}

type canvasProps = {
  str: string;
}

const App = () => {
  const displayRef = useRef<DisplayHandle>(null);
  const timerRef = useRef<TimerHandle>(null);
  const [num, setNum] = useState('25');
  var str = generateRandomString(Number(num));
  var index = 0
  useEffect(() => {
    displayRef.current!.drawString();
    window.addEventListener('keydown', (e) => {
      const char = e.key;
      if(e.keyCode < 32 || e.keyCode > 126) return;
      if(char === str[index]){
          displayRef.current!.changeColor(index, "red");
          index++;
          if(index === length){
              window.removeEventListener('keydown', (e) => {});
          }
      }else{
          for(;;){
              displayRef.current!.changeColor(index, "gray");
              if(index === 0) break;
              index--;
          }
      }
  })
  }, [str])
  return(
    <>
      <select onChange={e => setNum(e.target.value)}>
        <option value="25">25</option>
        <option value="50">50</option>
        <option value="100">100</option>
        <option value="200">200</option>
      </select>
      <Timer ref={timerRef} />
      <Display str={str} ref={displayRef} />
      <button onClick={() => {displayRef.current!.drawString()}}>write</button>
      <button onClick={() => {displayRef.current!.clearCanvas()}}>clear</button>
      <button onClick={() => {timerRef.current!.startTimer()}}>timer start</button>
      <button onClick={() => {timerRef.current!.stopTimer()}}>timer stop</button>
      <button onClick={() => {timerRef.current!.clearTimer()}}>timer clear</button>
      <button onClick={() => {sendPing}}>send ping</button>
    </>
  )
}

const generateRandomString = (len: number) => {
  var c = "abcdefghijklmnopqrstuvwxyz0123456789";
  
  var cl = c.length;
  var r = "";
  for(var i=0; i<len; i++){
      r += c[Math.floor(Math.random()*cl)];
  }
  return r;
}

export default App;