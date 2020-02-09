import React from 'react';
import './SearchBar.css';

class SearchBar extends React.Component {
  
  state = {input: ''};
  
  onInputChange(event) {
    console.log(event.target.value);
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
        <div className='field'>
        <label>Search me</label>
        <input 
         type="text"
         value={this.state.input}
         onChange={(e) => this.setState({input: e.target.value })} 
         /> 
        </div>
      </form>
    </div>
    )
  
  }
};

export default SearchBar;