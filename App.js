import logo from './logo.svg';
import './App.css';
import { useState } from 'react';

function App() {
  const [currentTime, setCurrentTime] = useState(0);

  result = fetch('/api').then(res => res.json())



  return (
    <div className="App">
      <header className="App-header">
        <button onClick={() => { handleClick(result) }}>Click Me!</button>
      </header>
    </div>
  );
}
function handleClick(result) {
  alert(result)
}


export default App;
