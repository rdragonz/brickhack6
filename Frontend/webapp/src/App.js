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
    <html>
      <body>
      <div className="App">
      <NavBar />
     
      <section className="searchbar-section">
        <SearchBar2 onSubmit={this.onSearchSubmit}/>
      </section>
      <section className="contentPane-section">
        <ContentPane />
      </section>
      </div> 
      </body>
      <footer>
       
     </footer>
    </html>
     
   
      
      
    
    
  );

  }
  
}

export default App;
