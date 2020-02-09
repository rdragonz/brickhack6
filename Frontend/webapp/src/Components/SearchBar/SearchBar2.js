import React from 'react';
import './SearchBar.css';
import { findDOMNode } from 'react-dom';
//import $ from 'jquery';

class SearchBar2 extends React.Component {
  
  state = {input: ''};
  
 

  onInputChange(event) {
    console.log(event.target.value);

    /*$('.ui.search')
    .search({
      source: content
    }); */
    
  }

  onInputClick(){
    console.log('Input was clicked');
  }

  onFormSubmit = (event) => {
    event.preventDefault();
    this.props.onSubmit(this.state.input);
  };


  render (){
    
    return (
      <div className='ui segment'>
        <form  className='ui form'>
          <div class="ui search">
           <div class="ui icon input">
            <input
              class="prompt" 
              type="text"
              placeholder="Seach Item..."
              value={this.state.input}
              onChange={(e) => this.setState({input: e.target.value })} 
              />
            <i class="search icon"></i>
          </div>
          <div class="results"></div>
        </div>
      </form>
    </div>
     
    )
  
  }
};

export default SearchBar2;