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

     <div id="content-container" class="container">
       <div class="container1">
       <div class="ui items">
      <div id="item"class="item">
        <div className="image">
          <img alt="image" src={faker.image.nature()}>
            </img>
        </div>
       
       <div id="test" class="content">
          <a class="header" href="#" >Content Pane 1</a>
          <div class="meta">
            <span>Description</span>
          </div>
          <div class="description">
            <p></p>
          </div>
          <div class="extra">
            Additional Details
          </div>
        </div>
      </div>
      </div>
       </div>
       


      
      <div class="ui items">
      <div class="item">
        <div class="image">
          <img src="/images/wireframe/image.png">
            </img>
        </div>
        <div class="content">
          <a class="header" href="#" >Content Pane 2</a>
          <div class="meta">
            <span>Description</span>
          </div>
          <div class="description">
            <p></p>
          </div>
          <div class="extra">
            Additional Details
          </div>
        </div>
      </div>
      </div>
     </div>

    )
  
  }
};

export default ContentPane;