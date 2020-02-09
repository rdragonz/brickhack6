import React from 'react';
import './App.css';
import SearchBar from './Components/SearchBar/SearchBar';
import SearchBar2 from './Components/SearchBar/SearchBar2';
import ContentPane from './Components/ContentPane/ContentPane';



<<<<<<< HEAD
function App() {
=======
class App extends React.Component{

  onSearchSubmit(input) {
    console.log(input);
  }

 render (){ 
>>>>>>> 7591b901d005266d39c447445da7e3e90b86bdb0
  return (
    <div className="App">
      {/*<SearchBar onSubmit={this.onSearchSubmit} /> */}
      <SearchBar2 onSubmit={this.onSearchSubmit}/>
      <ContentPane />
      <header className="App-header">
        Our Website 
      </header>
    </div>
  );
  }
}

export default App;
