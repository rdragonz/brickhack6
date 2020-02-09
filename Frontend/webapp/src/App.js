import React from 'react';
import './App.css';
import SearchBar from './Components/SearchBar/SearchBar';



<<<<<<< HEAD
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

=======

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
>>>>>>> 9ca85ed0e67e18c7fd385149d9a689bafbd9ee43
  }
  
}

export default App;
