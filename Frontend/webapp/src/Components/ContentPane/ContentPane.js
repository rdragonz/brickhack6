import React from 'react';
import './ContentPane.css';
import { findDOMNode } from 'react-dom';
//import $ from 'jquery';

class ContentPane extends React.Component {
  
  state = {input: ''};
  

  render (){
    
    return (
     <div class="container">
        <div class="ui items">
      <div class="item">
        <div class="image">
          <img src="/images/wireframe/image.png">
            </img>
        </div>
        <div class="content">
          <a class="header">Content Pane 1</a>
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
    
      <div class="ui items">
      <div class="item">
        <div class="image">
          <img src="/images/wireframe/image.png">
            </img>
        </div>
        <div class="content">
          <a class="header">Content Pane 3</a>
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