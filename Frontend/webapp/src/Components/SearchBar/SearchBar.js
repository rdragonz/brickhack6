import React from 'react';
import './SearchBar.css';

class SearchBar extends React.Component {
  
  state = {input: ''};
  
  onInputChange(event) {
    console.log(event.target.value);
  }
  render (){
    return (
      <div className="ui segment">
       <label>Item Search</label>
      <div className="ui category search">
        
      <div className="ui icon input">
        
        <input 
        className="prompt"
        type="text"
        placeholder="I am a noob">

          </input>
        <i className="search icon"></i>
      </div>
      <div className="results"></div>
    </div>
    </div>
    )
  
  }
};

export default SearchBar;