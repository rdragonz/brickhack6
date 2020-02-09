import React from 'react';
import './App.css';
import SearchBar from './Components/SearchBar/SearchBar';
import SearchBar2 from './Components/SearchBar/SearchBar2';
import ContentPane from './Components/ContentPane/ContentPane';



class App extends React.Component{

  onSearchSubmit(input) {
    console.log(input);
  }

 render (){ 
  return (
    <div className="App">
      {/*<SearchBar onSubmit={this.onSearchSubmit} /> */}
      <SearchBar2 onSubmit={this.onSearchSubmit}/>
      <ContentPane />
      <header className="App-header">
    
      </header>
    </div>
  );
  }
}

export default App;
