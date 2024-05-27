import { useRef, useImperativeHandle, forwardRef } from "react";

type canvasProps = {
  str: string;
}

export type DisplayHandle = {
  clearCanvas: () => void;
  drawString: () => void;
  changeColor: (index: number, color: string) => void;
}

const Display = forwardRef(function Display(props: canvasProps, ref) {
  var canvasRef = useRef<HTMLCanvasElement>(null);
  var str = props.str;
  var charFieldWidth = 20;
  var charFieldHeight = 40;
  const numberOfColumn = 25;
  var numberOfRow = Math.floor(str.length / numberOfColumn);
  const leftMargin = 5;
  const topMargin = 40;
  const charHeight = 20;
  const decender = 5;
  function clearCanvas() {
    var canvas = canvasRef.current!;
    var ctx = canvas.getContext("2d")!;
    ctx.clearRect(0, 0, canvas.width, canvas.height);
  }
  function drawString() {
    clearCanvas();
    var canvas = canvasRef.current!;
    var ctx = canvas.getContext("2d")!;
    var numberOfRow = Math.floor(str.length / numberOfColumn);
    ctx.font = charHeight.toString() + "px RobotoMono";
    ctx.fillStyle = "gray";
    for(var i = 0; i < numberOfRow; i++){
      for(var j = 0; j < numberOfColumn; j++){
        var index = numberOfColumn * i + j;
        var width = ctx.measureText(str[index]).width;
        ctx.fillText(str[index], leftMargin + j * charFieldWidth + (charFieldWidth - width) / 2, topMargin + i * charFieldHeight)
      }
    }
  }
  function changeColor(index: number, color: string) {
    var canvas = canvasRef.current!;
    var ctx = canvas.getContext("2d")!;
    var width = ctx.measureText(str[index]).width;
    ctx.clearRect(leftMargin + (index % numberOfColumn) * charFieldWidth, topMargin + Math.floor(index / numberOfColumn) * charFieldHeight + decender, charFieldWidth, -charFieldHeight);
    ctx.fillStyle = color;
    ctx.fillText(str[index], leftMargin + (index % numberOfColumn) * charFieldWidth + (charFieldWidth - width) / 2, topMargin + Math.floor(index / numberOfColumn) * charFieldHeight);
  }
  useImperativeHandle(ref, () => {
    return {
      clearCanvas, drawString, changeColor
    };
  });
  return (
    <div id='display'>
      <canvas id='canvas' ref={canvasRef} height="500px" width="1080px"></canvas>
    </div>
  );
});

export default Display;