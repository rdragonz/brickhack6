import React from 'react';
import './NavBar.css';
const navbar = () => {
  return (
    <header>
      <nav className="navbar">
        <div className="logo">Logo</div>
        <ul className="navLinks">
          <button className="btn"><a href='#'></a>Login/Register</button>
        </ul>
      </nav>
    </header>


  )
    
  
}

export default navbar;