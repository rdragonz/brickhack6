import React from 'react';
import './SearchBar2.css';
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
      <div id="test" className='ui segment'>
        <form id='test' className='ui form'>
         <div class="btn-container">
         <button class="ui button">Login/Register</button>
        </div> 
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