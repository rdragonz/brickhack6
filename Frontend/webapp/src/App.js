import React from 'react';
import './App.css';
import SearchBar from './Components/SearchBar/SearchBar';



class App extends React.Component {
  render (){
    return (
      <div className="App">
        <SearchBar/>
      
        <header className="App-header">
          Our Website 
        </header>
      </div>
    );

  }
  
}

export default App;
