import React from 'react';
import './App.css';
import SearchBar from './Components/SearchBar/SearchBar';
import SearchBar2 from './Components/SearchBar/SearchBar2';



class App extends React.Component{

  onSearchSubmit(input) {
    console.log(input);
  }

 render (){ 
  return (
    <div className="App">
      {/*<SearchBar onSubmit={this.onSearchSubmit} /> */}
      <SearchBar2 onSubmit={this.onSearchSubmit}/>
      <header className="App-header">
        Our Website 
      </header>
    </div>
  );
  }
}

export default App;
