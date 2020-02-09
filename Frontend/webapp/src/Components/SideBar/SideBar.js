import React from 'react';
import './SideBar.css';

class SideBar extends React.Component {
  render (){
    return (
      <div>
      <Row>
        <Col>1 of 3</Col>
        <Col xs={6}>2 of 3 (wider)</Col>
        <Col>3 of 3</Col>
      </Row>
      <Row>
        <Col>1 of 3</Col>
        <Col xs={5}>2 of 3 (wider)</Col>
        <Col>3 of 3</Col>
      </Row>
      </div>
    
    )
  
  }
};

export default SearchBar;