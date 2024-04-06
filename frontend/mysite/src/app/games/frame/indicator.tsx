'use client';

import { useEffect } from "react";

const number_of_frame = 60;
const number_of_color_specification = 255;
const milliseconds_in_one_frame = 16;

var clock: number;
var intervalId: number;
var startButton: HTMLButtonElement;
var stopButton: HTMLButtonElement;

export default function Indicator() {
  useEffect(() => {
    constructColorBar();
    buttonConfig();
  },[]);
  return (
    <div id="indicator"></div>
  )
}

function constructColorBar() {
  var indicator = document.getElementById("indicator") as HTMLDivElement;
  for(var i = 0; i <= number_of_frame; i++){
    var colorBox = document.createElement("div");
    var colorBar = document.createElement("div");
    colorBox.setAttribute("class", "colorBox");
    colorBar.setAttribute("class", "colorBar");
    colorBar.setAttribute("id", "bar" + String(i));
    colorBar.style.backgroundColor = "rgb(" + String(255 - Math.floor(number_of_color_specification / (number_of_frame + 1) * i)) + ", " + String(Math.floor(number_of_color_specification / (number_of_frame + 1) * i)) + ", 0, 1.0)"
    if(i == 0) {
      colorBar.style.visibility = 'visible';
    } else {
      colorBar.style.visibility = 'hidden';
    }
    colorBox.append(colorBar);
    indicator.append(colorBox);
  }
}
function buttonConfig() {
  startButton = document.getElementById("startButton") as HTMLButtonElement;
  stopButton = document.getElementById("stopButton") as HTMLButtonElement;
  startButton.addEventListener('click', startColoring);
  stopButton.addEventListener('click', stopColoring);
  stopButton.disabled = true;
}

function startColoring() {
  if(intervalId) clearInterval(intervalId);
  resetColorBar();
  intervalId = window.setInterval(execColoring, milliseconds_in_one_frame);
  stopButton.disabled = false;
}
function stopColoring() {
  clearInterval(intervalId);
  intervalId = 0;
  stopButton.disabled = true;
}
function resetColorBar() {
  clock = 0;
  for(var i = 1; i <= number_of_frame; i++){
    var colorBar = document.getElementById("bar" + String(i)) as HTMLDivElement;
    colorBar.style.visibility = 'hidden';
  }
}

function execColoring() {
  clock += 1;
  if(clock > number_of_frame){
    resetColorBar();
  }
  var currentBar = document.getElementById("bar" + String(clock)) as HTMLDivElement;
  currentBar.style.visibility = 'visible';
}