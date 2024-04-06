import Indicator from "./indicator";

export default function Frame() {
  return(
    <>
      <div id="display">
        <h2>1 Frame Command Trainer</h2>
        <Indicator/>
        <div id="buttons">
          <button id="startButton">start</button>
          <button id="stopButton">stop</button>
        </div>
      </div>
    </>
  )
}