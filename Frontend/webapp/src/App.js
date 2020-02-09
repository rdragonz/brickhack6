import React from 'react';
import './App.css';
import SearchBar2 from './Components/SearchBar/SearchBar2';
import ContentPane from './Components/ContentPane/ContentPane';
import NavBar from './Components/NavBar/NavBar';

class App extends React.Component{

  onSearchSubmit(input) {
    console.log(input);
  }

 render (){ 

  return (
    <div className="App">
      <NavBar />
      <SearchBar2 onSubmit={this.onSearchSubmit}/>
      <ContentPane />
      <header className="App-header">
    
      </header>
    </div>
  );

  }
  
}

export default App;
