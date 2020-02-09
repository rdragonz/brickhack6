import React from 'react';
import './App.css';
import SearchBar from './Components/SearchBar/SearchBar';



class App extends React.Component{

  onSearchSubmit(input) {
    console.log(input);
  }

 render (){ 
  return (
    <div className="App">
      <SearchBar onSubmit={this.onSearchSubmit} />
      <header className="App-header">
        Our Website 
      </header>
    </div>
  );
  }
}

export default App;
