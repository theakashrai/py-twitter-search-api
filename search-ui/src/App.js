import React from 'react';
import logo from './logo.svg';
import './App.css';
import Search from './Search';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
      </header>
      <Search/>
    </div>
  );
}

export default App;
