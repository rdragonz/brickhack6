import React from 'react';
import './ContentPane.css';
import { findDOMNode } from 'react-dom';
//import $ from 'jquery';
import faker from 'faker';


class ContentPane extends React.Component {
  
  state = {input: ''};
  


  render (){
    
    var faker = require('faker/locale/en');

    return (
      
      <div class="ui stackable three column grid">

      <div class="column">
         <div class="ui segment"> 
        <img src="./" 
        />
      </div>
      <a class="ui blue tag label">Tag</a>
      <a class="ui tag label">taggg</a>
      <a class="ui  tag label">Tagggggg</a>
     </div>

      <div class="column">
        <div class="ui segment">
        <img src="./" 
        />
        </div>
        <a class="ui teal tag label">New</a>
        <a class="ui tag label">Upcoming</a>
        <a class="ui teal tag label">Featured</a>
      </div>
      <div class="column">
        <div class="ui segment">
        <img src="./"
        />
        </div>
        <a class="ui teal tag label">New</a>
        <a class="ui tag label">Upcoming</a>
        <a class="ui teal tag label">Featured</a>
        </div>
    </div>
    

    )
  
  }
};

export default ContentPane;